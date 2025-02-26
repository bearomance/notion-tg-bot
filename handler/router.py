from service import notion_service, telegram_service
from datetime import datetime

class MessageRouter:
    def __init__(self):
        self.update = {}

    async def handle(self, update):
        print(f"Handling update: {update}")
        self.update = update
        message = update["message"]['text']
        notion_service.record(message,  datetime.now().isoformat())

        chat_id = update["message"]["chat"]["id"]
        await telegram_service.send_message(message, chat_id)
        return self