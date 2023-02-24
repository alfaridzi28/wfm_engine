from fastapi import FastAPI
import router
import asyncio

app = FastAPI(
    title="API WFM Engine"
)

@app.get("/")
async def index():
    res = "WFM Engine is started!"
    return res

app.include_router(router.route)
# asyncio.create_task(router.consume())
