from schemas import ChildrenInfo, StorySource, Interests
from db import children_info_collection, story_source_collection, interests_collection
from bson import ObjectId
from typing import List

#child_info
def get_child_info(id: str) -> dict:
    try:
        child_info = children_info_collection.find_one({"_id": ObjectId(id)})
        return {
            "id": str(child_info['_id']),
            "sex": child_info['sex'],
            "age": child_info['age'],
            "interests": child_info['interests']
        }
    except Exception as e:
        print("child info not found")

def get_all_children_infos() -> List[dict]:
    try:
        children_infos = children_info_collection.find()
        return [get_child_info(child_info['_id']) for child_info in children_infos]
    except Exception as e:
        print(" failed to read all chilren infos", e)

def create_child_info(children_info: ChildrenInfo):
    children_info_collection.insert_one(dict(children_info))

def update_child_info(id: str, children_info: ChildrenInfo):
    try:
        children_info_collection.find_one_and_update({"_id": ObjectId(id)}, {
            "$set": {
            "sex": children_info.sex,
            "age": children_info.age,
            "interests": children_info.interests
            }})
    except Exception as e:
        print("child info update failed", e)

def delete_child_info(id: str):
    try:
        children_info_collection.find_one_and_delete({"_id": ObjectId(id)})
        return {"status": 200}
    except Exception as e:
        print("child info delete failed", e)


#story_source
def get_story_source(id: str) -> dict:
    try:
        story_source = story_source_collection.find_one({"_id": ObjectId(id)})
        return {
            "id": str(story_source['_id']),
            "prompt": story_source['prompt'],
            "image_urls": story_source['image_urls']
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

def delete_story_source(id: str):
    story_source = story_source_collection.find_one({"_id": ObjectId(id)})
    story_source_collection.delete_one(story_source)


#interests
def get_interest(id: str) -> dict:
    interest = interests_collection.find_one({"_id": ObjectId(id)})
    return {
        "id": str(interest['_id']),
        "interest": interest['interest']
    }

def get_all_interests() -> List[dict]:
    interests = interests_collection.find()
    return [get_interest(interest['_id']) for interest in interests]

def create_interests(interests: Interests):
    interests_collection.insert_one(dict(interests))

def delete_interests(id: str):
    interests_collection.find_one_and_delete({"_id": ObjectId(id)})
