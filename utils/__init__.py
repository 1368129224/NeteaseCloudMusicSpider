import os
from pymongo import MongoClient
from config import MONGODB
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_client = MongoClient(MONGODB)
db = _client['NeteaseCloudMusicSpider']
