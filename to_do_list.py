def show_tasks(tasks):
    print("Tasks:")
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")


def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added successfully.")


def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task index.")


def todo_list():
    tasks = []

    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            show_tasks(tasks)
        elif choice == 2:
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == 3:
            show_tasks(tasks)
            task_index = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_index)
        elif choice == 4:
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list()
