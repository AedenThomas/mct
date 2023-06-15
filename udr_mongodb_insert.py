# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
from bson import json_util, ObjectId
import json

def udr_mongodb_insert (item):
    dbname = get_database()
    print("Insert subscriber info into UDR MongoDB:" ,dbname)
    sitem = json.loads(json_util.dumps(item))
    print("\nUDR Mongodb Inserted element:\n", sitem)
    collection_name = dbname["subscriber_entries"]
    collection_name.insert_one(sitem)
