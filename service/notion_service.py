import httpx
from datetime import datetime
from util.config import NOTION_TOKEN, NOTION_DATABASE_ID
from notion_client import Client
from model.page import Page


notion = Client(auth=NOTION_TOKEN)

def record(name, date):
    try:
        new_page = Page() \
            .title("Name", name) \
            .date("Date", date) \
            .build()
        notion.pages.create(parent={"database_id": NOTION_DATABASE_ID}, properties=new_page)
    except Exception as e:
        print(f"notion.pages.create ERROR: {e}")

if __name__ == "__main__":
    record("Hello, world!", datetime.now().isoformat())