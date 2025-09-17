from pymongo import MongoClient
from bson.objectid import ObjectId

# connection

MONGO_URI = "mongodb+srv://vetrichelvan468:root@cluster0.4wsuwmo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
database = client["pythonClass"]
collection = database["user"]

# userData = {
#     "name":"vetri",
#     "age":10,
#     "skill":"python",
#     "email":"vetri@gmail.com",
#     "mobile":8365378534
#     }


# students = [
#     {
#         "name": "Gowtham",
#         "age": 13,
#         "skill": "python,mongo",
#         "email": "gowtham@gmail.com",
#         "mobile": 8365378534,
#         "id": 101
#     },
#     {
#         "name": "Dhilip",
#         "age": 14,
#         "skill": "java,c++",
#         "email": "dhilip@gmail.com",
#         "mobile": 9876543210,
#         "id": 102
#     },
#     {
#         "name": "Vetri",
#         "age": 15,
#         "skill": "html,css,javascript",
#         "email": "vetri@gmail.com",
#         "mobile": 9123456789,
#         "id": 103
#     },
#     {
#         "name": "Arun",
#         "age": 16,
#         "skill": "python,flask",
#         "email": "arun@gmail.com",
#         "mobile": 9988776655,
#         "id": 104
#     },
#     {
#         "name": "Priya",
#         "age": 15,
#         "skill": "c,java",
#         "email": "priya@gmail.com",
#         "mobile": 8899776655,
#         "id": 105
#     },
#     {
#         "name": "Kavin",
#         "age": 14,
#         "skill": "javascript,react",
#         "email": "kavin@gmail.com",
#         "mobile": 7788996655,
#         "id": 106
#     },
#     {
#         "name": "Vimal",
#         "age": 15,
#         "skill": "nodejs,mongodb",
#         "email": "vimal@gmail.com",
#         "mobile": 9900112233,
#         "id": 107
#     }
# ]
# def student(name):
#     try:
#         for student in students:
#             if student["name"] == name: 
#                 print("Student found:", student)
#                 return student
#         raise ValueError("Student not found!")  
#     except KeyError as e:
#         print(f"Error: Missing key {e} in dictionary")
#     except ValueError as e:
#         print(e)
# student("Gowtham") 
# student("Arun")  
# student("Deepak")


# def deleteOne(id):
#     checkuser = collection.find_one({"_id":ObjectId(id)})
#     # print(checkuser)
#     Userdata = collection.delete_one({"_id":ObjectId(id)})
#     print(Userdata)

# deleteOne("68c818e17a48e1d591c0fc1f")


# def deleteOne(id):
#     try:
#         obj_id = ObjectId(id)
        
#         checkuser = collection.find_one({"_id": obj_id})
#         print("User found:", checkuser)
        
#         if checkuser:
#             Userdata = collection.delete_one({"_id": obj_id})
#             print("Delete result:", Userdata.deleted_count)
#         else:
#             print("No user found with this _id.")

#     except Exception as e:
#         print(f"Error occurred: {e}")

# deleteOne("68c426614ca1b786fe3f5865")


def deleteStudent(id):
    checkUser = collection.find_one({"_id":ObjectId(id)})
    print(checkUser)
    deleteUser = collection.delete_one({"_id":ObjectId(id)})
    print(deleteUser)

deleteStudent("68c426614ca1b786fe3f5865")