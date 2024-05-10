import sqlite3
connec = sqlite3.connect('ExProject.db')

query = ("CREATE TABLE IF NOT EXISTS tasks6 (pid INTEGER PRIMARY KEY, task TEXT NOT NULL, status TEXT NOT NULL);")
connec.execute(query)

def show():
    query = "SELECT * FROM tasks6;"
    return connec.execute(query)

def insertdata(ptask, pstatus):
    query = "INSERT INTO tasks6(task, status) VALUES(?,?);"
    connec.execute(query, (ptask, pstatus, ))
    connec.commit()

def deletetask(taskid):
    query = "DELETE FROM tasks6 WHERE pid =?;"
    connec.execute(query, (taskid,))
    connec.commit()

def updatetask(taskid, newstatus):
    query = "UPDATE tasks6 SET status = ? WHERE pid = ?;"
    connec.execute(query, (newstatus, taskid,))
    connec.commit()

def showID():
    query = "SELECT pid FROM tasks6;"
    print (connec.execute(query))

query2 = ("CREATE TABLE IF NOT EXISTS reg_users (pid INTEGER PRIMARY KEY, username TEXT NOT NULL, pw TEXT NOT NULL, name TEXT NOT NULL, email TEXT NOT NULL, age TEXT NOT NULL);")
connec.execute(query2)

def show_user():
    query2 = "SELECT * FROM reg_users;"
    return connec.execute(query2)

def insert_user(un, p_w, n_m, em, ag):
    query = "INSERT INTO reg_users(username, pw, name, email, age) VALUES(?,?,?,?,?);"
    connec.execute(query, (un, p_w, n_m, em, ag, ))
    connec.commit()