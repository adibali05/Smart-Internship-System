from pymongo import MongoClient
import certifi

# Yahan apna wahi purana MongoDB Atlas wala link rehne dena
MONGO_URL = "mongodb+srv://adibmuzammilali_db_user:<PASSWORD>@cluster0.s8zrt8j.mongodb.net/?appName=Cluster0" 

# tlsCAFile use karne se SSL error hamesha ke liye solve ho jayega
client = MongoClient(MONGO_URL, tlsCAFile=certifi.where())

db = client["internship_db"]
students_collection = db["students"]
logs_collection = db["logs"]

def init_db():
    if students_collection.count_documents({}) == 0:
        students_collection.insert_one({
            "student_id": "STU001",
            "name": "Karan Mehta",
            "company": "XYZ Corp",
        })
        print("MongoDB initialized with dummy data.")