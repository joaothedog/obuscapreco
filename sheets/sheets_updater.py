import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import GOOGLE_SHEETS_NAME, GOOGLE_CREDENTIALS_FILE
from alerts.telegram_alert import send_telegram_alert

def get_previous_prices(sheet):
    """
    Retorna um dicionário {url: preço_anterior}
    """
    try:
        records = sheet.get_all_records()
        return {row["URL"]: row["Preço Atual"] for row in records if row.get("URL")}
    except Exception as e:
        print("Erro ao buscar preços anteriores:", e)
        return {}

def parse_brl_to_float(price_str):
    if not price_str or "N/A" in price_str:
        return None
    try:
        # Remove "R$", espaços e pontos de milhar, troca vírgula por ponto decimal
        cleaned = price_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
        return float(cleaned)
    except:
        return None

def update_sheet(data):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    sheet = client.open(GOOGLE_SHEETS_NAME).sheet1

    # Obtém preços anteriores antes de limpar a planilha
    previous_data = get_previous_prices(sheet)

    # Limpa e escreve cabeçalho
    sheet.clear()
    sheet.append_row(["Site", "Produto", "Preço Atual", "Preço Anterior", "Diferença", "URL"])

    for item in data:
        url = item["url"]
        current_price = parse_brl_to_float(item["price"])
        prev_price = previous_data.get(url)
        prev_price_val = parse_brl_to_float(prev_price) if prev_price else None

        if current_price is not None and prev_price_val is not None:
            difference = current_price - prev_price_val
            difference_str = f'R$ {difference:,.2f}'.replace('.', ',')
            prev_str = f'R$ {prev_price_val:,.2f}'.replace('.', ',')
            # Envia alerta se preço caiu
            if difference < 0:
                send_telegram_alert(
                    f"📉 <b>{item['title']}</b>\n"
                    f"💰 <b>De:</b> {prev_str} | <b>Para:</b> {item['price']}\n"
                    f"🔗 <a href='{url}'>Ver produto</a>"
                )
        else:
            difference_str = "N/A"
            prev_str = "N/A"

        # Atualiza a planilha
        sheet.append_row([
            item["site"],
            item["title"],
            item["price"],
            prev_str,
            difference_str,
            url
        ])
