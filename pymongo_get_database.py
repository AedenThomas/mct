from pymongo import MongoClient
import urllib 



def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://testmongodb:testmongodb123@cluster0.hjhyvpk.mongodb.net/"
 
   print("Connecting to :", CONNECTION_STRING)
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING, connect=False)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_udm_database']
 
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":  
 
   # Get the database
   dbname = get_database()
   print("Database info:", dbname)
