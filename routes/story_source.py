from fastapi import APIRouter, UploadFile, File, Form
from schemas import StorySource
from typing import List
from s3 import upload_image_on_s3
from crud import create_story_source


import time

router = APIRouter(tags=['story'])

@router.post("/sources")
async def post_stroy_source(prompt: str = Form(), images: List[UploadFile] = File(...)): # (...) -> 생략부호
    image_urls = [upload_image_on_s3(image) for image in images]
    story_source = StorySource(prompt=prompt, image_urls=image_urls)
    create_story_source(story_source)

    pass