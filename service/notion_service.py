import httpx
from datetime import datetime
from util.config import NOTION_TOKEN, NOTION_DATABASE_ID
from notion_client import Client
from model.page import Page


class NotionService:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {NOTION_TOKEN}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        self.notion = Client(auth=NOTION_TOKEN)

    async def create_page(self, database_id, properties):
        """创建新的Notion页面/数据库条目"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://api.notion.com/v1/pages",
                headers=self.headers,
                json={
                    "parent": {"database_id": database_id},
                    "properties": properties
                }
            )
        return response.json()

    async def record(self, name, date):
        new_page = Page() \
            .title("Name", name) \
            .date("Date", date) \
            .build()
        self.notion.pages.create(parent={"database_id": NOTION_DATABASE_ID}, properties=new_page)


if __name__ == "__main__":
    import asyncio

    async def main():
        await NotionService().record("Test", datetime.now().isoformat())

    asyncio.run(main())