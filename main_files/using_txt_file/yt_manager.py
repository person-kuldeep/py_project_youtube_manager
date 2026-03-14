"""
Application_Name : youtube video watchlist manager 

Basic operations provided :

1. add video detail.
2. list all video details.
3. update video detail.
4. delete video detail.
5. Exit the application.

"""
import json

# txt to list converter
def load_data():
    try:
        with open("vid_data.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# list to txt update helper
def upload_data(updated_vid_data):
    with open("vid_data.txt", "w",) as file:
        json.dump(updated_vid_data, file)

#index input checking
def index_check(vid_data):
    list_det(vid_data)
    while True:
        vid_index = int(input("Select Index: "))
        if 0 < vid_index <= len(vid_data):
            return vid_index - 1
        else:
            print("\nINVALID INDEX\n")
            continue

# list all video details
def list_det(vid_data):
    print(f"Total videos: {len(vid_data)}")
    for index,vid_object in enumerate(vid_data, start=1):
        print(f"{index}. Title: {vid_object["title"]} , Duration: {vid_object["duration"]} minutes ")

# add new video detail
def add_det(vid_data):
    title = input("Enter Title: ")
    duration = input("Enter duration: ")
    vid_data.append({"title":title, "duration":duration})
    upload_data(vid_data)
    
    print(f"Title: {title} , Duration: {duration} minutes ---> Adding...")
    print("Video Added Successfully")

# update video detail
def update_det(vid_data):
    list_index = index_check(vid_data)
    
    print(f"  Title: {vid_data[list_index]["title"]} , Duration: {vid_data[list_index]["duration"]} minutes ")
    print("\n 1. Change Title")
    print(" 2. Change Duration")
    print(" 3. Change Both")
    inp = input("\nEnter the command ---> ") 
    match inp:
        case "1":
            title = input("Enter Title: ")
            vid_data[list_index] =  {"title":title, "duration":vid_data[list_index]["duration"]}
            upload_data(vid_data)
        case "2":
            duration = input("Enter duration: ")
            vid_data[list_index] =  {"title":vid_data[list_index]["title"], "duration":duration}
            upload_data(vid_data)
        case "3":
            title = input("Enter Title: ")
            duration = input("Enter duration: ")
            vid_data[list_index] =  {"title":title, "duration":duration}
            upload_data(vid_data)

        case _:
            print("\n\t\tINVALID COMMAND\n")

    print(f"Title: {vid_data[list_index]["title"]} , Duration: {vid_data[list_index]["duration"]} minutes ---> Updating...")
    print("Video Updated Successfully")

# delete video detail 
def delete_det(vid_data):
    list_index = index_check(vid_data)
    deleted_vid = vid_data.pop(list_index)
    upload_data(vid_data)
    print(f"Title: {deleted_vid["title"]} , Duration: {deleted_vid["duration"]} minutes ---> Deleting... ")
    print("Video Deleted Successfully")

# Main function 
def main():
    vid_data = load_data()
    print("\n***welcome to the application***\n")
    while True :
        print("")
        print("#"*100)

        print("\n#Insert the index number to select the command\n")
        print("1. List all video details.")
        print("2. Add video detail.")
        print("3. Update video detail.")
        print("4. Delete video detail.")
        print("5. Exit the application.\n")

        print("#"*100)

        inp = input("\nEnter the command ---> ") 
        match inp :
            case "1":
                list_det(vid_data)
                input("\npress any key to continue ")
            case "2":
                add_det(vid_data)
                input("\npress any key to continue ")
            case "3":
                update_det(vid_data)
                input("\npress any key to continue ")

            case "4":
                delete_det(vid_data)
                input("\npress any key to continue ")
            case "5": 
                print("\n :) Thanks for using the application\n")
                break
            case _:
                print("\n\t\tINVALID COMMAND\n")

    
if __name__ == "__main__":
    main()