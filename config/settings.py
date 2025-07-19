import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_SHEETS_NAME = os.getenv("GOOGLE_SHEETS_NAME", "Price Tracker")
GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_FILE", "credentials.json")
