from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId



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


add_selected_students(students,["Gowtham"])
