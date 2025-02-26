import requests

from util.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def send_message(text, chat_id=TELEGRAM_CHAT_ID):
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )
        print(response.json())
    except Exception as e:
        print(f"Error: {e}")


# async def send_message(text, chat_id=TELEGRAM_CHAT_ID):
#     print(f"Sending message: {text}, to chat_id: {chat_id}")
#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
#             json={"chat_id": chat_id, "text": text}
#         )
#     return response.json()
#
#
# async def send_button(text, buttons, chat_id=TELEGRAM_CHAT_ID):
#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
#             json={"chat_id": chat_id, "text": text, "reply_markup": {"keyboard": buttons, "one_time_keyboard": True}}
#         )
#     return response.json()
#
#
# if __name__ == "__main__":
#     import asyncio
#
#     async def main():
#         await send_message("Hello, world!")
#
#     asyncio.run(main())

if __name__ == "__main__":
    send_message("Hello, world!")