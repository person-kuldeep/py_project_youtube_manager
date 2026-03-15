import sqlite3

con = sqlite3.connect("yt_manager.db")

cur = con.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS video_details(
            video_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            duration INTEGER NOT NULL
            )
""")

def list_det():
    print("*"*100)
    cur.execute("""
                SELECT video_id,title,duration FROM video_details
                """)
    for row in cur.fetchall():
        print(row)
    print("*"*100)

def add_det(title,duration):
    cur.execute("INSERT INTO video_details (title, duration) VALUES (?, ?)", (title,duration))
    con.commit()

def update_det(video_id,new_title,new_duration):
    cur.execute("UPDATE video_details SET title = ?, duration = ? WHERE video_id = ? ", (new_title,new_duration,video_id))
    con.commit()

def delete_det(video_id):
    cur.execute("DELETE FROM video_details WHERE video_id = ?", (video_id,))
    con.commit()
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
                list_det()
                video_id = int(input("Enter video ID: "))
                new_title = input("Enter New Title: ")
                new_duration = int(input("Enter Duration: "))

                update_det(video_id, new_title,new_duration)

            case "4":
                list_det
                video_id = int(input("Enter video ID: "))
                delete_det(video_id)

            case "5":
                print("\n\t (: Thanks for using the application\n")
                break
            case _:
                print("\t INVALID COMMAND INPUT")        
    con.close()
if __name__ == "__main__":
    main()
