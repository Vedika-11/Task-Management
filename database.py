import sqlite3
from tabulate import tabulate
DB_NAME='task.db'

def connect_db():
    conn=sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY AUTOINCREMENT , 
                   description TEXT NOT NULL,
                   deadline TEXT , 
                   status TEXT DEFAULT 'Pending'
                   )

""")
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_NAME)


def add_task(description, deadline):
    conn=get_connection()
    cursor= conn.cursor()
    cursor.execute('INSERT INTO tasks (description , deadline) VALUES (?,?)',(description , deadline))
    conn.commit()
    conn.close()
    print("\nTask Added Successfully!")

def view_task():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks=cursor.fetchall()
    conn.close()
    if tasks:
        print(tabulate(tasks, headers=['ID' , 'Description' , 'Deadline' , 'Status'], tablefmt='grid'))
    else:
        print('\nNo Tasks are Found!')

def view_pending_tasks():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE status="Pending"')
    tasks=cursor.fetchall()
    conn.close

    if tasks:
        print(tabulate(tasks, headers=['ID' ,'Description' , 'Deadline' ,'Status'], tablefmt="grid"))
    else:
        print("\nNo Pending Task Found!")

def view_completed_tasks():
    conn=get_connection()
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE status='Completed'")
    tasks=cursor.fetchall()
    conn.close()
    if tasks:
        print(tabulate(tasks, headers=["ID", "Description", "Deadline", "Status"], tablefmt="grid"))
    else:
        print("\nNo Completed Tasks Found.")

def update_task(task_id , new_description=None , mark_completed=False):
    conn=get_connection()
    cursor=conn.cursor()
    if new_description:
        cursor.execute("UPDATE tasks SET description=? where id=?", (new_description, task_id))
        print("\nNew Description Updated Successfully!")
    if mark_completed:
        cursor.execute("UPDATE tasks SET status='Completed' WHERE ID=?",(task_id ,))
        print("\nTask Marked Completed Successfully!")
    conn.commit()
    conn.close()

def delete(task_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?",(task_id ,))
    conn.commit()
    conn.close()
    print("\nTask Deleted Successfully!")

def search_taks(keyword):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE description LIKE ?",('%' + keyword + '%' ,))
    tasks=cursor.fetchall()
    conn.close()
    if tasks:
        print(tabulate(tasks , headers=['ID' , 'Description' , 'Deadline' , 'Status'], tablefmt="grid"))
    else:
        print("\nNo Such Task Found!")

def sort_task():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY deadline ASC ")
    tasks= cursor.fetchall()
    conn.close()
    if tasks:
        print(tabulate(tasks , headers=['ID' , 'Description' , 'Deadline' , 'Status'] , tablefmt="grid"))
    else:
        print("\nNo Task Found!")


