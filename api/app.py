import uvicorn
from fastapi import FastAPI

from loguru import logger

from db.connection import Session
from info.views import info_router
from user.views import user_router


app = FastAPI()
logger.add("test.log", rotation="100 MB")

app.include_router(info_router)
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
