from fastapi import APIRouter, UploadFile, File, Form
from schemas import StorySource
from typing import List
from s3 import upload_image_on_s3
from crud import get_all_story_sources, get_story_source, create_story_source, delete_story_source


import time

router = APIRouter(tags=['story_source'])

@router.get("/sources")
async def fetch_all_story_sources():
    return get_all_story_sources()

@router.get("/sources/{id}")
async def fetch_story_source(id: str):
    return get_story_source(id)

@router.post("/sources")
async def post_stroy_source(prompt: str = Form(), images: List[UploadFile] = File(...)): # (...) -> 생략부호
    image_urls = [upload_image_on_s3(image) for image in images]
    story_source = StorySource(prompt=prompt, image_urls=image_urls)
    create_story_source(story_source)

@router.delete("/sources/{id}")
async def remove_story_source(id: str) -> None:
    delete_story_source(id)