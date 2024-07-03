from db import story_source_collection
from schemas import StorySource
from bson import ObjectId
from typing import List


def get_story_source(id: str) -> dict:
    try:
        story_source = story_source_collection.find_one({"_id": ObjectId(id)})
        return {
            "id": str(story_source['_id']),
            "prompt": story_source['prompt']
        }
    except Exception as e:
        print("story source not found", e)


def get_all_story_sources() -> List[dict]:
    try:
        story_sources = story_source_collection.find()
        return [get_story_source(story_source['_id']) for story_source in story_sources]
    except Exception as e:
        print("read all story sources failed", e)


def create_story_source(story_source: StorySource):
    story_source_collection.insert_one(dict(story_source))
    # TODO: GPT, DALLE에 소스 전달하고 [샘플제목, 카테고리, 샘플 표지 이미지] 받음


def delete_story_source(id: str):
    story_source = story_source_collection.find_one({"_id": ObjectId(id)})
    story_source_collection.delete_one(story_source)
