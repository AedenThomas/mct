# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["subscriber_entries"]

item_1 = {
  "name" : "yourname1",
  "imsi" : "1122334455",
  "state" : "KA",
  "roaming" : "Y"
}

item_2 = {
  "name" : "yourname2",
  "imsi" : "43434344455", 
  "state" : "KA",
  "roaming" : "Y"
}

print("\nInsert elements:\n")
collection_name.insert_many([item_1,item_2])
