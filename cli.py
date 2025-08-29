from models import User, Task

def main():
    while True:
        print("\n--- Task Manager CLI ---")
        print("1. Manage Users")
        print("2. Manage Tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            task_menu()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def user_menu():
    while True:
        print("\n--- User Menu ---")
        print("1. Create User")
        print("2. View Users")
        print("3. Find User by ID")
        print("4. Delete User")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter user name: ")
            User.create(name)
            print("User created.")
        elif choice == "2":
            users = User.get_all()
            table = [(u.id, u.name) for u in users]
            print(tabulate(table, headers=["ID", "Name"]))
        elif choice == "3":
            uid = int(input("Enter user ID: "))
            user = User.find_by_id(uid)
            print(user.name if user else "Not found.")
        elif choice == "4":
            uid = int(input("Enter user ID: "))
            User.delete(uid)
            print("User deleted.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def task_menu():
    while True:
        print("\n--- Task Menu ---")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Find Task by ID")
        print("4. Delete Task")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            uid = int(input("Enter user ID: "))
            Task.create(title, uid)
            print("Task created.")
        elif choice == "2":
            tasks = Task.get_all()
            table = [(t.id, t.title, t.status, t.user_id) for t in tasks]
            print(tabulate(table, headers=["ID", "Title", "Status", "User ID"]))
        elif choice == "3":
            tid = int(input("Enter task ID: "))
            task = Task.find_by_id(tid)
            if task:
                print(f"{task.id}: {task.title} [{task.status}] (User {task.user_id})")
            else:
                print("Not found.")
        elif choice == "4":
            tid = int(input("Enter task ID: "))
            Task.delete(tid)
            print("Task deleted.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
