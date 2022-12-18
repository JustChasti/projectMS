from fastapi import APIRouter
from fastapi.responses import JSONResponse


info_router = APIRouter()


@info_router.get('/info/worked', response_class=JSONResponse)
async def check_service():
    data = {
        'info': 'service worked!!!'
    }
    return data
