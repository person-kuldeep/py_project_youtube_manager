from pymongo import MongoClient


client = MongoClient("mongodb+srv://pythonproject:pythonproject@cluster0.tlf8cdu.mongodb.net/")

db = client["yt_manager"]

video_det = db["videos"]

# print(video_det)

def list_det():
    print("*"*100)
    obj_id = []
    for index,video in enumerate(video_det.find(), start=1):
        obj_id.append(video["_id"])
        print(f"{index}. Title: {video["title"]} Duration: {video["duration"]} minutes")
    print("*"*100)
    # print(type(obj_id[0])) <class 'bson.objectid.ObjectId'>
    return obj_id 

def add_det(title,duration):
    video_det.insert_one({"title": title, "duration": duration})
    
def update_det(video_id,new_title,new_duration):
    video_det.update_one({"_id": video_id}, {"$set": {"title": new_title, "duration": new_duration}})

def delete_det(video_id):
    video_det.delete_one({"_id": video_id})


def main():
    print("\n *** Welcome to Youtube Video Manager ***")
    while True :
        print("""
### COMMANDS\n
 1. List all videos
 2. Add new video
 3. Update existing video
 4. Delete existing video 
 5. Exit the Application
""")
        
        c_inp = input("Enter The  Command: ")

        match c_inp:
            case "1":
                list_det()
            case "2":
                title = input("Enter Title: ")
                duration = int(input("Enter Duration: "))

                add_det(title, duration)

            case "3":
                obj_id = list_det()
                video_id = int(input("Enter video ID: "))
                video_id = obj_id[video_id-1]
                new_title = input("Enter New Title: ")
                new_duration = int(input("Enter Duration: "))

                update_det(video_id, new_title,new_duration)

            case "4":
                obj_id = list_det()
                video_id = int(input("Enter video ID: "))
                video_id = obj_id[video_id-1]
                delete_det(video_id)

            case "5":
                print("\n\t (: Thanks for using the application\n")
                break
            case _:
                print("\t INVALID COMMAND INPUT")      


if __name__ == "__main__":
    main()