from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.qjqyxd3.mongodb.net/", tlsAllowInvalidCertificates=True)
db = client["ytmanager"]
video_collection = db["videos"]


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_video():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video["name"]}, and Time: {video["time"]}")

def update_video(video_id, name, time):
    video_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": name , "time":time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_video()
        elif choice == "2":
            name = input("Enter video name:")
            time = input("Enter video time:")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video id to update:")
            name = input("Enter the updated video name:")
            time = input("Enter the updated video time:")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video id to delete:")
            delete(video_id)
        elif choice == "4":
            break
        else: 
            print("Invalid Choice")
if __name__ == "__main__":
    main()