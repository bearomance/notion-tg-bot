from service import notion_service, telegram_service



class MessageRouter:
    def __init__(self):
        self.update = {}
        self.notion = notion_service.NotionService()

    def handle(self, update):
        print('Handling update')
        self.update = update
        self.notion.record('test', '2022-06-28')

        message = update["message"]
        chat_id = message["chat"]["id"]
        telegram_service.send_message(message['text'], chat_id)
        return self