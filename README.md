# Projeto: Busca de Preços Automática com Alertas no Telegram

## Descrição

Este projeto automatiza a busca de preços de produtos na Amazon, atualiza uma planilha no Google Sheets com os dados coletados e envia alertas via Telegram quando há queda de preço.

Ideal para monitorar variações de preço e ser notificado instantaneamente quando um produto ficar mais barato.

---

## Funcionalidades

- **Scraping de preços da Amazon**: coleta o título, preço e URL dos produtos usando Selenium e BeautifulSoup.
- **Atualização automática do Google Sheets**: mantém uma planilha atualizada com as informações atuais e registra os preços anteriores para comparar diferenças.
- **Comparação de preços**: calcula a diferença entre o preço atual e o preço salvo anteriormente.
- **Alertas via Telegram**: envia mensagem automática para um grupo ou chat via bot do Telegram quando o preço de um produto cai.
- **Configuração segura com `.env`**: armazena credenciais e tokens sensíveis fora do código-fonte.
- **`.gitignore` configurado**: evita o upload acidental de arquivos sensíveis como credenciais e variáveis de ambiente.

---

## Tecnologias utilizadas

- Python 3.x
- Selenium
- BeautifulSoup
- Google Sheets API (via `gspread` e `oauth2client`)
- Telegram Bot API (via `requests`)
- `python-dotenv` para variáveis de ambiente

---

## Como usar

### 1. Configuração do ambiente

Clone este repositório e crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt

---

### 2. Configuração das credenciais Google Sheets

- Crie um projeto no Google Cloud Console
- Ative as APIs Google Sheets e Google Drive
- Crie uma conta de serviço e faça download do arquivo JSON das credenciais
- Renomeie o arquivo para credentials.json e coloque na raiz do projeto
- Compartilhe sua planilha Google Sheets com o email da conta de serviço

---

### 3. Configuração do bot Telegram

- Crie um bot pelo @BotFather no Telegram
- Anote o token do bot
- Crie ou utilize um grupo no Telegram, adicione o bot e obtenha o chat_id do grupo (use o método getUpdates da API Telegram)

### 4. Variáveis de ambiente


`GOOGLE_SHEETS_NAME=Nome da sua planilha`

`GOOGLE_CREDENTIALS_FILE=credentials.json`

`TELEGRAM_TOKEN=seu_token_aqui`

`TELEGRAM_CHAT_ID=seu_chat_id_aqui`


### 5. Executar o projeto

`python main.py`

