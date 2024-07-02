from fastapi import APIRouter
from schemas import Interests
from crud import get_all_interests, get_interest, create_interests, delete_interests

router = APIRouter(tags=['interests'])

@router.get("")
async def fetch_all_interests():
    return get_all_interests()

@router.get("/{id}")
async def fetch_interest(id: str):
    return get_interest(id)

@router.post("")
async def post_interest(interests: Interests):
    create_interests(interests)

@router.delete("/{id}")
async def remove_interests(id: str):
    delete_interests(id)