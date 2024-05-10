import myDatab
import os
import sqlite3
connec = sqlite3.connect('ExProject.db')

os.system("clear")

print("\t---- MENU -----\n")
print("\t1. Register yourself\n\t2. Signin\t")
opt = int(input("\nEnter your preferred choice from above given Menu\n\t> "))
if (opt == 1):
    username = input("Enter your username: ")
    passw = input("Enter password: ")
    name = input("Enter Name: ")
    email = input("Enter email: ")
    age = input("Enter age: ")
    myDatab.insert_user(username, passw, name, email, age)
    print("\nRegistered successfully!\n")
    
if (opt == 2):
    cur = connec.cursor() 
    username = input("Enter your username: ")
    passw = input("Enter password: ")
    query = f"SELECT username from reg_users WHERE username ='{username}' AND pw = '{passw}';"
    cur.execute(query) 
    if not cur.fetchone():
        print("Login Failed!") 
    else: 
        print("Login Successful!\n")    
        print("\t---- WELCOME TO TASK MANAGER ----\n")
        print("\t1. View Task(s)\n\t2. Add Task\n\t3. Delete Task\n\t4. Update Task\n\t5. Exit\t")
        ch = int(input("\nEnter your preferred choice from above given Menu\n\t> "))

        while ch != 5:

            if (ch == 1):
                print("\nID" + "\t" + "TASK" + "\t" + "STATUS\n")
                for rows in myDatab.show():
                    print(str(rows[0]) + "\t" + rows[1] + "\t" + rows[2])
                ch = int(input("\nEnter your preferred choice from above given Menu\n\t> "))

            elif (ch == 2):
                task_user = input("Enter A Task: ")
                status_user = input("Enter A Status: ")
                if(len(task_user) != 0):
                    myDatab.insertdata(task_user, status_user)
                    print("\nTask successfully inserted!")
                ch = int(input("\nEnter your preferred choice from above given Menu\n\t> "))
                
            elif(ch == 3):
                print("\nID" + "\t" + "TASK" + "\t" + "STATUS\n")
                for rows in myDatab.show():
                    print(str(rows[0]) + "\t" + rows[1] + "\t" + rows[2])
                id = int(input("\nChoose A Task ID To Delete: "))
                cur = connec.cursor() 
                query = f"SELECT pid from tasks6 WHERE pid ='{id}';"
                cur.execute(query) 
                if not cur.fetchone():
                    print ("Task not available!")
                else:
                    myDatab.deletetask(id)
                    print("\nTask successfully deleted!")
                ch = int(input("\nEnter your preferred choice from above given Menu\n\t> "))

            elif (ch == 4):
                print("\nID" + "\t" + "TASK" + "\t" + "STATUS\n")
                for rows in myDatab.show():
                    print(str(rows[0]) + "\t" + rows[1] + "\t" + rows[2])
                id = int(input("\nChoose A Task ID To Update it: "))
                cur = connec.cursor() 
                query = f"SELECT pid from tasks6 WHERE pid ='{id}';"
                cur.execute(query) 
                if not cur.fetchone():
                    print ("Task not available!")
                else:
                    newstat = (input("Enter new status: "))
                    myDatab.updatetask(id, newstat)
                    print("\nTask successfully updated!")
                ch = int(input("\nEnter your preferred choice from above given Menu\n\t> "))

            else:
                print("\nChoose the right option please!")
                ch = int(input("\nEnter your preferred choice from above given Menu\n\t> "))

        else:
            print("\nThank You For Using This Application\n")