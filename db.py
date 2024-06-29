from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
MONGODB_URL = os.getenv('MONGODB_URL')
client = MongoClient(MONGODB_URL)

db = client.story_generator_db

children_info_collection = db['child_info_collection']
prompt_collection = db['prompt_collection']


