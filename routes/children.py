from fastapi import APIRouter
from schemas import ChildrenInfo
from crud import create_child_info, read_child_info, update_child_info, delete_child_info
import time

router = APIRouter(tags=['children'])

@router.get("/children/{id}")
async def fetch_child_info(id: str):
    return read_child_info(id)

@router.post("/children")
async def post_child_info(children_info: ChildrenInfo):
    await create_child_info(children_info)

@router.patch("/children/{id}")
async def edit_child_info(id: str, children_info: ChildrenInfo):
    update_child_info(id, children_info)

@router.delete("/children/{id}")
async def remove_child_info(id: str):
    delete_child_info(id)


