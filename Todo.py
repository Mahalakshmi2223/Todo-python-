import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file"""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("✅ No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do CLI App ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("✅ Task added!")
        elif choice == "3":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Deleted: {deleted}")
                else:
                    print("❌ Invalid number!")
            except ValueError:
                print("❌ Please enter a number!")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option, try again!")

if __name__ == "__main__":
    main()
