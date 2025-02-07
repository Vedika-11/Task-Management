import database
from database import *

def main():
    database.connect_db()

    while True:
        print("\nTask Management Application")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. View Completed Tasks")
        print("5. Update a Task")
        print("6. Delete a Task")
        print("7. Sort Tasks")
        print("8. Search For a Task")
        print("9. Exit")

        choice = int(input("\nEnter Your Choice:"))

        if choice == 1:
            description = input("\nEnter Task Description:")
            deadline= input("\nEnter Task Deadline (YYYY-MM-DD , Optional):")
            add_task(description, deadline)
        elif choice ==2:
            view_task()
        elif choice == 3:
            view_pending_tasks()
        elif choice ==4:
            view_completed_tasks()
        elif choice == 5:
            task_id=int(input("\nEnter Task Id:"))
            print("1. Mark Completed")
            print("2. Edit Description")
            update_choice= int(input("Choose an Option:"))
            if update_choice==1:
                update_task(task_id, mark_completed=True)
            elif update_choice==2:
                new_description = input("Enter New Description")
                update_task(task_id, new_description)
            else:
                print("Choose Correct Option!")
        elif choice ==6:
            task_id=int(input("Enter the Task Id To Delete:"))
            delete(task_id)
        elif choice ==7:
            sort_task()
        elif choice ==8:
            keyword = input("Enter keyword Through Which You Want To Search Task:")
            search_taks(keyword)
        elif choice == 9:
            print("Exiting Application!")
            break
        else:
            print("\nInvalid Choice ! Please Try Again.")
if __name__ =="__main__":
    main()


            