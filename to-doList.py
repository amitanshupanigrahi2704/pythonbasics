def todo_list():
    tasks = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            if tasks:
                print("Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks found.")
        elif choice == '3':
            if tasks:
                task_num = int(input("Enter the task number to remove: "))
                if 0 < task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to remove.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

todo_list()
