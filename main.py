from fastapi import FastAPI, Request
import asyncio
from handler.router import MessageRouter

app = FastAPI()
router = MessageRouter()


@app.get("/")
async def ping():
    return {"message": "Hello, World!"}

@app.post("/webhook")
async def webhook(request: Request):
    try:
        update = await request.json()
        print(f"Telegram webhook received update: {update}")
        asyncio.create_task(router.handle(update))
    except Exception as e:
        print(f"解析JSON时出错: {e}")
    return {"status": "ok"}