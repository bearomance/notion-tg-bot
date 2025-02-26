import os
from dotenv import load_dotenv

if os.environ.get('VERCEL', False):
    print('In Vercel environment')
else:
    print('Not in Vercel environment, loading .env file')
    load_dotenv()

# Telegram配置
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

# Notion配置
NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
NOTION_DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "")

# AI API配置
API_KEY = os.environ.get("API_KEY", "")
API_HOST = os.environ.get("API_HOST", "https://api.openai.com")
API_MODEL = os.environ.get("API_MODEL", "gpt-3.5-turbo")