import asyncio
import sys

from motor import motor_asyncio
from LunaRobot import MONGO_DB_URI 
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from LunaRobot.Config import get_int_key, get_str_key
from LunaRobot import LOGGER as log

MONGO_PORT = get_int_key("27018")
MONGO_DB_URI = get_str_key("MONGO_DB_URI")
MONGO_DB = "LunaRobot"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["LunaRobot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
