
import json
import os
import time

TASKS_FILE = "tasks.json"


def clear_screen():
    """Clears the console screen for a cleaner interface."""
    os.system('cls' if os.name == 'nt' else 'clear')


def load_tasks():
    """Loads tasks from TASKS_FILE, creating the file if it doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        print("First run: Creating a new 'tasks.json' file.")
        time.sleep(1)
        return []
    try:
        # Using with ensures the file is closed properly
        with open(TASKS_FILE, 'r') as f:
            # Handle case where the file is empty
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading tasks file: {e}. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except IOError as e:
        print(f"FATAL ERROR: Could not save tasks. {e}")


def display_tasks(tasks):
    """Displays all current tasks in a formatted way."""
    clear_screen()
    print("✨ Your To-Do List ✨")
    print("=" * 25)
    if not tasks:
        print("\nYour to-do list is empty. Add a task!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status_icon = "✅" if task['completed'] else "🔲"
            print(f"{idx}. {status_icon} {task['description']}")
    print("\n" + "=" * 25)


def add_task(tasks):
    """Prompts user to add a new task."""
    description = input("Enter the new task description: ").strip()
    if description:
        tasks.append({"description": description, "completed": False})
        save_tasks(tasks)
        print(f"\n✅ Task '{description}' was added!")
    else:
        print("\n❌ Error: Task description cannot be empty.")
    time.sleep(1.5)


def update_task_status(tasks, mark_as_complete):
    """Marks a task as either complete or incomplete."""
    action = "complete" if mark_as_complete else "incomplete"
    display_tasks(tasks)
    if not tasks:
        print("No tasks to update.")
        time.sleep(1.5)
        return

    try:
        task_num_str = input(f"Enter task number to mark as {action}: ").strip()
        if not task_num_str:
            print("\n❌ Canceled. No input provided.")
            time.sleep(1.5)
            return

        task_num = int(task_num_str)
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = mark_as_complete
            save_tasks(tasks)
            print(f"\n✅ Task {task_num} marked as {action}.")
        else:
            print("\n❌ Error: Invalid task number.")
    except ValueError:
        print("\n❌ Error: Please enter a valid number.")

    time.sleep(1.5)


def delete_task(tasks):
    """Removes a task from the list."""
    display_tasks(tasks)
    if not tasks:
        print("No tasks to delete.")
        time.sleep(1.5)
        return

    try:
        task_num_str = input("Enter the task number to DELETE: ").strip()
        if not task_num_str:
            print("\n❌ Canceled. No input provided.")
            time.sleep(1.5)
            return

        task_num = int(task_num_str)
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"\n🗑️ Task '{removed_task['description']}' was deleted.")
        else:
            print("\n❌ Error: Invalid task number.")
    except ValueError:
        print("\n❌ Error: Please enter a valid number.")

    time.sleep(1.5)


def main():
    """The main application loop."""
    tasks = load_tasks()
    while True:
        display_tasks(tasks)
        print("\nMenu:")
        print("1. Add a new task")
        print("2. Mark a task as complete")
        print("3. Mark a task as incomplete")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task_status(tasks, True)
        elif choice == '3':
            update_task_status(tasks, False)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nGoodbye! Keep up the great work! 👋")
            break
        else:
            print("\n❌ Invalid choice. Please select a number from 1 to 5.")
            time.sleep(1.5)


if __name__ == "__main__":
    main()
