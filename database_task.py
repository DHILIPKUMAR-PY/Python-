from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId



MONGO_URI = "mongodb+srv://dhilipkumar:dhilipkumar@cluster0.q5lks8c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
database = client["pythonClass"]
collection = database["user"]


students =[
  {
    "name": "Gowtham",
    "age": 13,
    "total marks": 500,
    "email": "gowtham@gmail.com",
    "mobile": 8365378534,
    "roll no": 605013
  },
  {
    "name": "Ananya",
    "age": 14,
    "total marks": 480,
    "email": "ananya@gmail.com",
    "mobile": 9876543210,
    "roll no": 605014
  },
  {
    "name": "Rahul",
    "age": 13,
    "total marks": 455,
    "email": "rahul@gmail.com",
    "mobile": 9123456780,
    "roll no": 605015
  },
  {
    "name": "Sneha",
    "age": 14,
    "total marks": 490,
    "email": "sneha@gmail.com",
    "mobile": 9988776655,
    "roll no": 605016
  },
  {
    "name": "Arjun",
    "age": 13,
    "total marks": 470,
    "email": "arjun@gmail.com",
    "mobile": 9876501234,
    "roll no": 605017
  },
  {
    "name": "Meena",
    "age": 12,
    "total marks": 465,
    "email": "meena@gmail.com",
    "mobile": 9345678123,
    "roll no": 605018
  },
  {
    "name": "Vikram",
    "age": 14,
    "total marks": 440,
    "email": "vikram@gmail.com",
    "mobile": 9001234567,
    "roll no": 605019
  },
  {
    "name": "Divya",
    "age": 13,
    "total marks": 495,
    "email": "divya@gmail.com",
    "mobile": 9234567890,
    "roll no": 605020
  },
  {
    "name": "Karthik",
    "age": 13,
    "total marks": 430,
    "email": "karthik@gmail.com",
    "mobile": 9012345678,
    "roll no": 605021
  },
  {
    "name": "Priya",
    "age": 12,
    "total marks": 485,
    "email": "priya@gmail.com",
    "mobile": 9123987654,
    "roll no": 605022
  }
]

def createStudentsData(a):
    print(a)
    res = collection.insert_many(a)
    print("students added!!!")

# createStudentsData(students)


def arranged_order():
    datas = collection.find().sort("total marks",-1)
    for i in datas:
        print(i)
arranged_order()

