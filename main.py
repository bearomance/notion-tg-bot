from fastapi import FastAPI, Request
import asyncio
from handler.router import MessageRouter
from service import telegram_service
from datetime import datetime, timezone, timedelta

app = FastAPI()
router = MessageRouter()


@app.get("/")
async def ping():
    return {"message": "Hello, World!"}

@app.post("/webhook")
async def webhook(request: Request):
    try:
        update = await request.json()
        asyncio.create_task(router.handle(update))
    except Exception as e:
        print(f"Handle webhook ERROR: {e}")
    return {"status": "ok"}

@app.post("/cron")
async def cron():
    try:
        current_time = datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8)))
        telegram_service.send_message(f"Current time is: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        return {"status": "success", "message": "Cron job executed successfully"}
    except Exception as e:
        print(f"Cron job ERROR: {e}")
        return {"status": "error", "message": str(e)}