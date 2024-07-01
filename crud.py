from schemas import ChildrenInfo, StorySource
from db import children_info_collection, story_source_collection
from bson import ObjectId

#child_info
def create_child_info(children_info: ChildrenInfo):
    children_info_collection.insert_one(dict(children_info))

def read_child_info(id: str):
    try:
        child_info = children_info_collection.find_one({"_id": ObjectId(id)})
        return {
            "sex": child_info['sex'],
            "age": child_info['age'],
            "interests": child_info['interests']
        }
    except Exception as e:
        print("child info not found")

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
def create_story_source(story_source: StorySource):
    story_source_collection.insert_one(dict(story_source))