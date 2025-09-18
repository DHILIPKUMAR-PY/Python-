from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId
# connection

MONGO_URI = "mongodb+srv://dhilipkumar:dhilipkumar@cluster0.q5lks8c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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


students = [
    {
        "name": "Gowtham",
        "age": 13,
        "skill": "python,mongo",
        "email": "gowtham@gmail.com",
        "mobile": 8365378534,
        "id": 101
    },
    {
        "name": "Dhilip",
        "age": 14,
        "skill": "java,c++",
        "email": "dhilip@gmail.com",
        "mobile": 9876543210,
        "id": 102
    },
    {
        "name": "Vetri",
        "age": 15,
        "skill": "html,css,javascript",
        "email": "vetri@gmail.com",
        "mobile": 9123456789,
        "id": 103
    },
    {
        "name": "Arun",
        "age": 16,
        "skill": "python,flask",
        "email": "arun@gmail.com",
        "mobile": 9988776655,
        "id": 104
    },
    {
        "name": "Priya",
        "age": 15,
        "skill": "c,java",
        "email": "priya@gmail.com",
        "mobile": 8899776655,
        "id": 105
    },
    {
        "name": "Kavin",
        "age": 14,
        "skill": "javascript,react",
        "email": "kavin@gmail.com",
        "mobile": 7788996655,
        "id": 106
    },
    {
        "name": "Vimal",
        "age": 15,
        "skill": "nodejs,mongodb",
        "email": "vimal@gmail.com",
        "mobile": 9900112233,
        "id": 107
    }
]
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



#Task
# # Student adding
# userData = {
#     "name":"vetri",
#     "age":10,
#     "skill":"python",
#     "email":"vetri@gmail.com",
#     "mobile":8365378534
#     }

# userData = {
#     "name":"vetri",
#     "age":10,
#     "skill":"python",
#     "email":"vetri@gmail.com",
#     "mobile":8365378534
#     }

# def add_student(student_id):
#     try:
#         if userData ["name"] == student_id["name"]:
#             print("User is found;",userData ["name"])

#         else:
#             print("User is not found:")
#         res = collection.insert_one(student_id)
#         print("User is inserted:",res.inserted_id)
    
#     except Exception as e:
#         print("Error",str (e))

# add_student(userData)

students = [
    {
        "name": "Gowtham",
        "age": 13,
        "skill": "python,mongo",
        "email": "gowtham@gmail.com",
        "mobile": 8365378534,
        "id": 101
    },
    {
        "name": "Dhilip",
        "age": 14,
        "skill": "java,c++",
        "email": "dhilip@gmail.com",
        "mobile": 9876543210,
        "id": 102
    },
    {
        "name": "gokul",
        "age": 15,
        "skill": "c,java",
        "email": "gokul@gmail.com",
        "mobile": 8899776655,
        "id": 105
    },
   
]
def add_selected_students(students_list, name_insert):
    try:
        selected = [s for s in students_list if s["name"] in name_insert]

        if not selected:
            print("Student not found")
            return
        result = collection.insert_many(selected)
        for student, inserted_id in zip(selected, result.inserted_ids):
            print(f"Inserted: {student['name']} (id: {inserted_id})")

    except Exception as e:
        print("Error inserting students:", str(e))


# add_selected_students(students,["Dhilip"])

def deleteStudent(id):
    try:
        obj_id = ObjectId(id)

        checkUser = collection.find_one({"_id": obj_id})
        if not checkUser:
            print("User not found")
        else:
            print("User found:", checkUser)

            deleteUser = collection.delete_one({"_id": obj_id})
            if deleteUser.deleted_count > 0:
                print("User deleted successfully")
            else:
                print("Failed to delete user")
    except InvalidId:
        print("Invalid ObjectId")
    except Exception as e:
        print("Database error:", str(e))
deleteStudent("68c818e17a48e1d591c0fc1f")




# def deleteStudent(id):
#     checkUser = collection.find_one({"_id":ObjectId(id)})
#     deleteUser = collection.delete_one({"_id":ObjectId(id)})
#     print(deleteUser)

# deleteStudent()





# #Update

# newupdate ={
#     "name" : "vetri",
#     "age" : 16
# }

# def updatestudent(id,newchange):
#     user = collection.find_one({"_id":ObjectId(id)})
#     updateUser = collection.update_one({"_id":ObjectId(id)},{"$set":newchange})
#     print(updateUser)

# updatestudent("68c426614ca1b786fe3f5865",newupdate)


#sort:-
# def sortData():
#     data = collection.find().sort("name",-1)
#     for i in data:
#         print(i)
# sortData()


#Query:-
# def sortData():
#     query = {"age": {"$gt": 13}}  
#     data = collection.find(query).sort("age", -1)
#     for i in data:
#         print(i)
# sortData()

# Type2:-
# def sortData():
#     query = {"age": {"$lt": 21}}  
#     data = collection.find(query).sort("age", -1)
#     for i in data:
#         print(i)
# sortData()

#Type3:-
# def sortData():
#     query = {"age": {"$lte": 21}}  
#     data = collection.find(query).sort("age", -1)
#     for i in data:
#         print(i)
# sortData()

#Type4:-
# def sortData():
#     query = {"age": {"$gte": 11}}  
#     data = collection.find(query).sort("age", -1)
#     for i in data:
#         print(i)
# sortData()


# Type5:-
# def sortData():
#     query = {"age": {"$ne": 11}}  
#     data = collection.find(query).sort("age", -1)
#     for i in data:
#         print(i)
# sortData()