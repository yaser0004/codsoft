class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append([task, False])
        print("Task added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, (task, completed) in enumerate(self.tasks, 1):
                print(f"{i}. {task} [{'COMPLETED' if completed else 'INCOMPLETE'}]")

    def mark_completed(self, n):
        if 0<n<= len(self.tasks):
            self.tasks[n-1][1] = True
            print("Task marked as completed.")

    def delete_task(self, n):
        if 0<n<= len(self.tasks):
            self.tasks.pop(n-1)
            print("Task deleted.")

todo=ToDoList()
while True:
    action=input("\n1. Add a new task \n2. View the Task list \n3. Mark task as 'Complete' \n4. Delete task \n5. Exit \nChoose an option: ")
    if action=="1":
        todo.add_task(input("Enter task: "))
    elif action=="2":
        todo.view_tasks()
    elif action=="3":
        todo.view_tasks()
        todo.mark_completed(int(input("Task number to mark complete: ")))
    elif action=="4":
        print("\nCurrent tasks:")
        todo.view_tasks()
        todo.delete_task(int(input("Task number to delete: ")))
    elif action=="5":
        print("End.")
        break
