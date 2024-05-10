import myDatab
import sqlite3
connec = sqlite3.connect('ExProject.db')
from email.mime import image
import tkinter 
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from numpy import place
import re

#main window k liye hai

main = Tk()
main.title("TASK MANAGER")
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
x_coordinate = (screen_width - 500) // 2
y_coordinate = (screen_height - 500) // 2
main.geometry(f"500x500+{x_coordinate}+{y_coordinate}")

main.resizable(False, False)
main.configure(
    background="#FFFFFF",
)

image= Image.open("E:\\OS LAB\\OS Project\\IMG\\tasksss.png")
image= image.resize((500,500))
photo = ImageTk.PhotoImage(image)
img = Label(main, image=photo, text='Middle', relief="flat")
img.pack(padx=1, pady=1)
img.place(x=250, y=250, anchor='center')
img.lift()
Label(
    main,
    text="Task Manager",
    background="gray94",
    foreground="#655C80",
    font=("Calibri 30"),
    
).pack(pady=30)

#signup click kr k jo ata
def openNewWindow(*args):
            main.withdraw()
            new = Toplevel(main)
            new.title("TASK MANAGER")
            new.geometry("800x600")
            new.resizable(False, False)
            new.configure(
            background="#E1E0F4",
            )

            Label(
            new,
            text="Task Manager",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 30"),
            ).pack(pady=20)
            Label(
            new,
            text="Username:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=200, y=100)

            inputtxt = Text(new,
            height=2,
            width=25)
            inputtxt.pack()
            inputtxt.place(x=350, y=100)

            Label(
            new,
            text="Password:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=200, y=170)
            password_var = StringVar()
            password_entry = Entry(new, textvariable=password_var, show="*", width= 33)
            password_entry.place(x=350, y=173, height=35)

            Label(
            new,
            text="Name:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=200, y=240)

            inputtxt = Text(new,
            height=2,
            width=25)
            inputtxt.pack()
            inputtxt.place(x=350, y=240)

            def validate_email(value):
                email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
                return bool(re.match(email_pattern, value))

            
            Label(
            new,
            text="Email:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=200, y=310)
            email_var = StringVar()
            def on_email_focusout(event):
                if not validate_email(email_var.get()):
                    messagebox.showerror("Invalid Email", "Please enter a valid email address")
            email_entry = Entry(new, textvariable=email_var, width=33)
            email_entry.place(x=350, y=310,height=35)
            email_entry.bind("<FocusOut>", on_email_focusout)

            def validate_age(value, action):
                if action == '1':  
                    try:
                        int(value)
                        return True
                    except ValueError:
                        return False
                return True

            Label(
            new,
            text="Age:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=200, y=380)
            age_var = StringVar()
            age_entry = Entry(new, textvariable=age_var, width=33, validate="key", validatecommand=(new.register(validate_age), '%P', '%d'))
            age_entry.place(x=350, y=383, height=35)

            def register_user():
                username = inputtxt.get("1.0", "end-1c").strip()
                password = password_var.get()
                name = inputtxt.get("1.0", "end-1c").strip()  # Change to the correct entry widget
                email = email_var.get().strip()
                age = age_var.get()

                # Additional validation
                if not all([username, password, name, email, age]):
                    messagebox.showerror("Registration Error", "Please fill in all fields.")
                    return

                try:
                    connec = sqlite3.connect('ExProject.db')
                    cursor = connec.cursor()
                    cursor.execute("SELECT * FROM reg_users WHERE username=?", (username,))
                    if cursor.fetchone():
                        messagebox.showerror("Registration Error", "Username already exists. Please choose a different one.")
                        return

                    # Enhance email validation
                    if not email or not validate_email(email):
                        messagebox.showerror("Invalid Email", "Please enter a valid email address")
                        return


                    cursor.execute("INSERT INTO reg_users (username, pw, name, email, age) VALUES (?, ?, ?, ?, ?)",
                                (username, password, name, email, age))
                    connec.commit()
                    connec.close()

                    messagebox.showinfo("Registration Successful", "User registered successfully!")
                    new.destroy()
                    main.deiconify()

                except Exception as e:
                    messagebox.showerror("Database Error", f"Error during registration: {str(e)}")
            #for second window and will link to login page
            addbtn = Button(
            new,
            text="Signup",
            background="#007aa5",
            foreground="#FFF",
            width = 15,
            relief="flat",
            font=("Calibri 14"),
            command=register_user
            )
            addbtn.pack(padx=10)
            addbtn.place(x=400, y=480, anchor='center')
            
            addbtn = Button(
            new,
            text="Back to Main Menu",
            background="#007aa5",
            width= 15,
            foreground="white",
            relief="flat",
            font=("Calibri 14"),
            command=lambda: [new.destroy(),main.deiconify()]
            
            )
            addbtn.pack(padx=10)
            addbtn.place(x=30, y=530)
            
            addbtn = Button(
            new,
            text="Quit",
            background="#007aa5",
            width= 5,
            foreground="white",
            relief="flat",
            font=("Calibri 14"),
            command=main.destroy
            )
            addbtn.pack(padx=10)
            addbtn.place(x=700, y=530)
                         
#login k baad aegi
def openNewWindow2(*args):
            
            main.withdraw()
            new1 = Toplevel(main)
            new1.title("TASK MANAGER")
            new1.geometry("800x600")
            new1.resizable(False, False)
            new1.configure(
            background="#E1E0F4",
            )
            Label(
            new1,
            text="Task Manager",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 30"),
            ).pack(pady=20)

            Label(
            new1,
            text="Username:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=200, y=200)

            username_entry = Text(new1, height=2, width=25)
            username_entry.pack()
            username_entry.place(x=350, y=200)

            Label(
            new1,
            text="Password:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=200, y=300)
            password_var = StringVar()
            password_entry = Entry(new1, textvariable=password_var, show="*", width= 33)
            password_entry.pack(pady=(20,30))
            password_entry.place(x=350, y=310, height=35)
            
            def login():
                    entered_username = username_entry.get("1.0", "end-1c")
                    entered_password = password_var.get()
                    cur = connec.cursor()
                    query = f"SELECT username from reg_users WHERE username = '{entered_username}' AND pw = '{entered_password}';"
                    cur.execute(query)
                    if not cur.fetchone():
                            messagebox.showerror("Login Error", "Invalid username or password")
                    else:
                            new1.destroy()
                            openNewWindow3()


            addbtn = Button(
            new1,
            text="Login",
            background="#007aa5",
            foreground="#FFF",
            width= 15,
            relief="flat",
            font=("Calibri 14"),
            command = login
            )
            addbtn.pack(padx=10)
            addbtn.place(x=400, y=430, anchor='center')

            addbtn = Button(
            new1,
            text="Back to Main Menu",
            background="#007aa5",
            width= 15,
            foreground="white",
            relief="flat",
            font=("Calibri 14"),
            command=lambda: [new1.destroy(),main.deiconify()]
            
            )
            addbtn.pack(padx=10)
            addbtn.place(x=30, y=530)
            
            addbtn = Button(
            new1,
            text="Quit",
            background="#007aa5",
            width= 5,
            foreground="white",
            relief="flat",
            font=("Calibri 14"),
            command=main.destroy
            )
            addbtn.pack(padx=10)
            addbtn.place(x=700, y=530)
            
def openNewWindow3(*args):
            main.withdraw()
            new2 = Toplevel(main)
            new2.title("TASK MANAGER")
            new2.geometry("800x600")
            new2.resizable(False, False)
            new2.configure(
            background="#E1E0F4",
            )
            
            Label(
            new2,
            text="Task Manager",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 30"),
            ).pack(pady=20)
            
            Label(
            new2,
            text="Choose one option",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=150, y=110, anchor='center')

            Label(
            new2,
            text="1.",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 16"),
            ).place(x=120, y=175)

            l1 = Label(
            new2,
            text="Add Task",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 16 underline"),
            cursor="hand2"
            )
            l1.place(x=200, y=175)
            l1.bind("<Button-1>", lambda event, current_window=new2: openNewWindow4(current_window))

            #second button
            Label(
            new2,
            text="2.",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 16"),
            ).place(x=120, y=250)
            l1 = Label(
            new2,
            text="View Task",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 16 underline"),
            cursor="hand2"
            )
            l1.place(x=200, y=250)
            l1.bind("<Button-1>", lambda event, current_window=new2: openNewWindow5(current_window))

            #update button
            Label(
            new2,
            text="3.",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 16"),
            ).place(x=120, y=330)
            l1 = Label(
            new2,
            text="Update Task",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 16 underline"),
            cursor="hand2"
            )
            l1.place(x=200, y=330)
            l1.bind("<Button-1>", lambda event, current_window=new2: openNewWindow6(current_window))

            #Delete Task  button
            Label(
            new2,
            text="4.",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 16"),
            ).place(x=120, y=410)

            l1 = Label(
            new2,
            text="Delete Task",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 16 underline"),
            cursor="hand2"
            )
            l1.place(x=200, y=410)
            l1.bind("<Button-1>", lambda event, current_window=new2: openNewWindow7(current_window))
           
            addbtn = Button(
            new2,
            text="Back to Login ",
            background="#007aa5",
            width= 15,
            foreground="white",
            relief="flat",
            font=("Calibri 14"),
            command=lambda: [new2.withdraw(),openNewWindow2()]
            
            )
            addbtn.pack(padx=0)
            addbtn.place(x=30, y=530)
            
            addbtn = Button(
            new2,
            text="Quit",
            background="#007aa5",
            width= 5,
            foreground="white",
            relief="flat",
            font=("Calibri 14"),
            command=main.destroy
            )
            addbtn.pack(padx=0)
            addbtn.place(x=700, y=530)
                    
def openNewWindow4(current_window):
            current_window.destroy()
            new3 = Toplevel(main)
            new3.title("TASK MANAGER")
            new3.geometry("800x600")
            new3.resizable(False, False)
            new3.configure(
            background="#E1E0F4",
            )
            
            Label(
            new3,
            text="Task Manager",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 30"),
            ).pack(pady=20)
            
            Label(
            new3,
            text="Task Details",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=300, y=100)

            Label(
            new3,
            text="ID:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=150, y=200)
            validate_id = new3.register(lambda s: s.isdigit() or s == "" and len(s) <= 5)
            id_entry = Entry(new3,width=33 ,validate="key", validatecommand=(validate_id, "%P"))
            id_entry.place(x=350, y=200, height=35)

            Label(
            new3,
            text="Task Name:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=150, y=300)
            name_entry = Entry(new3, width=33)
            name_entry.place(x=350, y=300, height=35)

            Label(
            new3,
            text="Status:",
            background="#E1E0F4",
            foreground="#363547",
            font=("Calibri 20"),
            ).place(x=150, y=400)
            status_var = StringVar()
            status_options = ["Active", "Paused", "Completed"]  # Add more options as needed
            status_dropdown = ttk.Combobox(new3,width=31, textvariable=status_var, values=status_options)
            status_dropdown.place(x=350, y=400, height=35)

            def add_task_to_database(task_id, task_name, task_status):
                # Connect to the SQLite database
                conn = sqlite3.connect('ExProject.db')
                cursor = conn.cursor()

                try:
                    # Execute the INSERT query
                    cursor.execute("INSERT INTO tasks6 (task, status) VALUES (?, ?)", (task_name, task_status))
                    conn.commit()
                    messagebox.showinfo("Success", "Task added to the database successfully!")
                except sqlite3.Error as e:
                    messagebox.showerror("Error", f"Error inserting task into the database: {e}")
                finally:
                    # Close the database connection
                    conn.close()

            addbtn = Button(
            new3,
            text="Add Task",
            background="#007aa5",
            width= 15,
            foreground="white",
            relief="flat",
            font=("Calibri 14"),
            command=lambda: [add_task_to_database(id_entry.get(), name_entry.get(), status_var.get()), new3.destroy(), openNewWindow3()]
            )
            addbtn.pack(padx=10)
            addbtn.place(x=330, y=480)

            addbtn = Button(
            new3,
            text="Back",
            background="#007aa5",
            width= 15,
            foreground="white",
            relief="flat",
            font=("Calibri 14"),
            command=lambda: [new3.destroy(),openNewWindow3()]
            
            )
            addbtn.pack(padx=0)
            addbtn.place(x=30, y=530)
            
            addbtn = Button(
            new3,
            text="Quit",
            background="#007aa5",
            width= 5,
            foreground="white",
            relief="flat",
            font=("Calibri 14"),
            command=main.destroy
            )
            addbtn.pack(padx=0)
            addbtn.place(x=700, y=530)

#after clicking view task, open new window
def openNewWindow5(current_window):
    current_window.destroy()
    new4 = Toplevel(main)
    new4.title("TASK MANAGER")
    new4.geometry("800x600")
    new4.resizable(False, False)
    new4.configure(
        background="#E1E0F4",
    )
    Label(
        new4,
        text="Task Manager",
        background="#E1E0F4",
        foreground="#363547",
        font=("Calibri 30"),
    ).pack(pady=20)
    def display_tasks(tasks):
        new_window = Toplevel(main)
        new_window.title("All Tasks")
        new_window.geometry("400x300")

        if tasks:
            task_list = "\n".join([f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}" for task in tasks])
        else:
            task_list = "No tasks found."

        label_tasks = Label(new_window, text=task_list, font=("Calibri", 14))
        label_tasks.pack(pady=20)
        

        close_button = Button(new_window, text="Close", command=new_window.destroy)
        close_button.pack(pady=10)

    def fetch_all_tasks():
        try:
            tasks = myDatab.show()
            display_tasks(tasks)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching tasks: {str(e)}")

    def display_tasks_by_id(task_id):
        
        try:
        
            query = f"SELECT * FROM tasks6 WHERE pid = {task_id};"
            task = connec.execute(query).fetchone()

            if task:
                new_window = Toplevel(main)
                new_window.title(f"Task ID: {task_id}")
                new_window.geometry("400x150")

                task_info = f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}"
                label_task_info = Label(new_window, text=task_info, font=("Calibri", 14))
                label_task_info.pack(pady=20)

                close_button = Button(new_window, text="Close", command=new_window.destroy)
                close_button.pack(pady=10)
            else:
                messagebox.showinfo("Task Not Found", f"No task found with ID: {task_id}")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching task: {str(e)}")

   
    def fetch_task_by_id():
        try:
            task_id = id_entry.get() 
            display_tasks_by_id(task_id)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for task ID.")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching tasks: {str(e)}")


    # Button to fetch all tasks
    fetch_all_btn = Button(
        new4,
        text="Fetch All Tasks",
        background="#007aa5",
        width=15,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=fetch_all_tasks
    )
    fetch_all_btn.pack(pady=10)
    fetch_all_btn.place(x=330, y=200)

    Label(
        new4,
        text="Enter ID:",
        background="#E1E0F4",
        foreground="#363547",
        font=("Calibri 18"),
    ).place(x=270, y=290)
    id_entry = Entry(new4, width=26)
    id_entry.pack(pady=10)
    id_entry.place(x=380, y=300)

    # Button to fetch task by ID
    fetch_by_id_btn = Button(
        new4,
        text="Fetch Task by ID",
        background="#007aa5",
        width=15,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=fetch_task_by_id
    )
    fetch_by_id_btn.pack(pady=10)
    fetch_by_id_btn.place(x=330, y=350)

    addbtn = Button(
        new4,
        text="Back",
        background="#007aa5",
        width=15,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=lambda: [new4.destroy(), openNewWindow3()]
    )
    addbtn.pack(pady=10)
    addbtn.place(x=30, y=530)

    addbtn = Button(
        new4,
        text="Quit",
        background="#007aa5",
        width=5,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=main.destroy
    )
    addbtn.pack(pady=10)
    addbtn.place(x=700, y=530)

#after clicking updating task, open new window
def openNewWindow6(current_window):
    
    current_window.destroy()
    new5 = Toplevel(main)
    new5.title("TASK MANAGER")
    new5.geometry("800x600")
    new5.resizable(False, False)
    new5.configure(
        background="#E1E0F4",
    )
    def fetch_task_by_id(taskid):
        query = "SELECT * FROM tasks6 WHERE pid = ?;"
        return connec.execute(query, (taskid,)).fetchone()

    def updatetask(taskid, newstatus):
        query = "UPDATE tasks6 SET status = ? WHERE pid = ?;"
        connec.execute(query, (newstatus, taskid,))
        connec.commit()
    
    Label(
        new5,
        text="Task Manager",
        background="#E1E0F4",
        foreground="#363547",
        font=("Calibri 30"),
    ).pack(pady=20)

    Label(
        new5,
        text="Enter Task ID:",
        background="#E1E0F4",
        foreground="#363547",
        font=("Calibri 20"),
    ).place(x=150, y=200)

    inputtxt = Text(
        new5,
        height=2,
        width=19)
    inputtxt.place(x=450, y=200)

    
    def fetch_task():
        task_id = inputtxt.get("1.0", "end-1c").strip()
        task_details = fetch_task_by_id(task_id)

        if task_details:
           
            name_entry.delete(0, END)
            name_entry.insert(0, task_details[1]) 

            # Set the status dropdown to the fetched status
            status_var.set(task_details[2])  # Assuming status is at index 2
        else:
            open_popup("Task not found!")

    # Function to handle updating the task
    def update_task():
        task_id = inputtxt.get("1.0", "end-1c").strip()
        new_status = status_var.get()

        updatetask(task_id, new_status)

        open_popup("Task updated!")

    # Entry field for name
    name_entry = Entry(
        new5,
        width=25,
    )
    name_entry.place(x=450, y=250, height=35)

    # Dropdown menu for status
    status_options = ["Active", "Paused", "Completed"]  # Add your status options here
    status_var = StringVar(new5)
    status_var.set(status_options[0])  # Set default status
    status_dropdown = OptionMenu(new5, status_var, *status_options)
    status_dropdown.place(x=450, y=300)

    # Fetch button
    fetch_btn = Button(
        new5,
        text="Fetch",
        background="#007aa5",
        width=15,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=fetch_task
    )
    fetch_btn.pack(pady=10)
    fetch_btn.place(x=330, y=350)

    # Update button
    update_btn = Button(
        new5,
        text="Update",
        background="#007aa5",
        width=15,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=update_task
    )
    update_btn.pack(pady=10)
    update_btn.place(x=330, y=400)

    # Back and Quit buttons
    back_btn = Button(
        new5,
        text="Back",
        background="#007aa5",
        width=15,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=lambda: [new5.destroy(), openNewWindow3()]
    )
    back_btn.pack(pady=10)
    back_btn.place(x=30, y=530)

    quit_btn = Button(
        new5,
        text="Quit",
        background="#007aa5",
        width=5,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=main.destroy
    )
    quit_btn.pack(pady=10)
    quit_btn.place(x=700, y=530)

# Function to open a popup message
def open_popup(message):
    popup = Toplevel(main)
    popup.title("Message")
    popup.geometry("200x80")
    popup.resizable(False, False)
    popup.configure(
        background="#fffafa",
    )
    Label(
        popup,
        text=message,
        background="#fffafa",
        foreground="#100c08",
        font=("Courier 12"),
    ).pack(pady=20)

#after clicking delete task, open new window
def openNewWindow7(current_window):
    current_window.destroy()
    new6 = Toplevel(main)
    new6.title("TASK MANAGER")
    new6.geometry("800x600")
    new6.resizable(False, False)
    new6.configure(
        background="#E1E0F4",
    )
    Label(
        new6,
        text="Task Manager",
        background="#E1E0F4",
        foreground="#363547",
        font=("Calibri 30"),
    ).pack(pady=20)

    Label(
        new6,
        text="Enter Task ID:",
        background="#E1E0F4",
        foreground="#363547",
        font=("Calibri 20"),
    ).place(x=150, y=200)

    inputtxt = Text(
        new6,
        height=2,
        width=25)
    inputtxt.place(x=450, y=200)

    def open_pop2(message):
        check1 = Toplevel(main)
        check1.title("Message")
        check1.geometry("200x80")
        check1.resizable(False, False)
        check1.configure(
            background="#fffafa",
        )
        Label(
            check1,
            text=message,
            background="#fffafa",
            foreground="#100c08",
            font=("Courier 12"),
        ).pack(pady=20)

    def delete_task_by_id():
        task_id = inputtxt.get("1.0", END).strip()
        if task_id:
            myDatab.deletetask(taskid=task_id)
            open_pop2("Task deleted!")
        else:
            open_pop2("Please enter a Task ID.")

    def delete_all_tasks():
        query = "DELETE FROM tasks6;"
        connec.execute(query)
        connec.commit()
        open_pop2("All tasks deleted!")

    # Button to delete a specific task
    delete_btn = Button(
        new6,
        text="Delete Task",
        background="#007aa5",
        foreground="white",
        width=15,
        relief="flat",
        font=("Calibri 14"),
        command=delete_task_by_id
    )
    delete_btn.pack(padx=10)
    delete_btn.place(x=330, y=280)

    # Button to delete all tasks
    delete_all_btn = Button(
        new6,
        text="Delete All",
        background="#007aa5",
        foreground="white",
        width=15,
        relief="flat",
        font=("Calibri 14"),
        command=delete_all_tasks
    )
    delete_all_btn.pack(padx=10)
    delete_all_btn.place(x=500, y=280)

    back_btn = Button(
        new6,
        text="Back",
        background="#007aa5",
        width=15,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=lambda: [new6.destroy(), openNewWindow3()]
    )
    back_btn.pack(pady=10)
    back_btn.place(x=30, y=530)

    quit_btn = Button(
        new6,
        text="Quit",
        background="#007aa5",
        width=5,
        foreground="white",
        relief="flat",
        font=("Calibri 14"),
        command=main.destroy
    )
    quit_btn.pack(pady=10)
    quit_btn.place(x=700, y=530)
       
#for main window
addbtn = Button(
            main,
            text="Signup",
            background="#007aa5",
            width= 10,
            foreground="#FFFFFF",
            relief="flat",
            font=("Calibri 14"),
            command=openNewWindow
        )
addbtn.pack(padx=10)
addbtn.place(x=170, y=450, anchor='center')

addbtn = Button(
            main,
            text="Login",
            background="#007aa5",
            foreground="#FFFFFF",
            width= 10,
            relief="flat",
            font=("Calibri 14"),
            command=openNewWindow2
        )
addbtn.pack(padx=20)
addbtn.place(x=330, y=450, anchor='center')
    

main.mainloop()