# LIFO (stack)

# Create a task manager in python using stack with basic functionalities:
#  (classes, methods, lists, loops, input-handling in python )
#  - add tasks with a title and description (enqueue)
#  - mark tasks as completed (dequeue)
#  - display the list of tasks along with status
#  - exit option to exit the task manager


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False  # Initially, the task is not completed


class TaskManager: #buong stack
    def __init__(self):
        self.task_stack = []  # Using a list as a stack to store tasks

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.task_stack.append(new_task)
        print(f"Task '{title}' added successfully!")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.task_stack):
            self.task_stack[task_index].completed = True
            print(f"Task '{self.task_stack[task_index].title}' marked as completed.")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if not self.task_stack:
            print("No tasks to display.")
        else:
            print("List of Tasks:")
            for i, task in enumerate(self.task_stack):
                status = "Completed" if task.completed else "Pending"
                print(f"{i + 1}. {task.title} - {task.description} [{status}]")

    def run_task_manager(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. Mark Task as Completed")
            print("3. Display Tasks")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                self.add_task(title, description)
            elif choice == "2":
                task_index = int(input("Enter task index to mark as completed: "))
                self.mark_task_completed(task_index - 1)  # Adjust index to match list indexing
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 to 4.")


# Example usage:
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run_task_manager()
