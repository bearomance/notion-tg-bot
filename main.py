from fastapi import FastAPI, Request
import asyncio
from handler.router import MessageRouter
from service import telegram_service

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
async def cron_job():
    try:
        # 在这里添加您想要每小时执行的任务
        print("Running hourly cron job")
        # 例如：await router.some_hourly_task()
        telegram_service.send_message("Hello, World!")
        return {"status": "success", "message": "Cron job executed successfully"}
    except Exception as e:
        print(f"Cron job ERROR: {e}")
        return {"status": "error", "message": str(e)}