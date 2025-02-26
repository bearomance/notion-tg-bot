from service import notion_service, telegram_service
from datetime import datetime

class MessageRouter:
    def __init__(self):
        self.update = {}

    async def handle(self, update):
        print('Handling update')
        self.update = update
        message = update["message"]['text']
        chat_id = message["chat"]["id"]

        notion_service.record(message,  datetime.now().isoformat())

        await telegram_service.send_message(message, chat_id)
        return self