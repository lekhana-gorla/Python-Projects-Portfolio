class Todolist:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print("Task added successfully.")

    def remove_task(self, task):
        for t in self.tasks:
            if t['task'] == task:
                self.tasks.remove(t)
                print("Task removed successfully.")
                return
        print("Task not found.")

    def mark_completed(self, task):
        for t in self.tasks:
            if t['task'] == task:
                t['completed'] = True
                print("Task marked as completed.")
                return
        print("Task not found in the list.")

    def display_tasks(self):
        if self.tasks:
            print('Tasks:')
            for i, t in enumerate(self.tasks, start=1):
                status = 'Completed' if t['completed'] else 'Not completed'
                print(f"{i}. {t['task']} - {status}")
        else:
            print("No tasks in the list.")


def main():
    todo_list = Todolist()
    while True:
        print("\nTODO LIST MENU:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Display the tasks")
        print("5. Exit")

        choice = input("Enter your choice 1-5: ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            task = input("Enter the task to mark as completed: ")
            todo_list.mark_completed(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()

import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task):
        if task.strip() != "":
            self.tasks.append({"task": task, "completed": False})
            self.save_tasks()
            return True
        return False

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
            return True
        return False

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            return True
        return False

    def save_tasks(self):
        with open(self.filename, "w") as f:
            for t in self.tasks:
                f.write(f"{t['task']}|{t['completed']}\n")

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    task, completed = line.strip().split("|")
                    self.tasks.append({"task": task, "completed": completed == "True"})
        except FileNotFoundError:
            pass


class TodoApp:
    def __init__(self, root):
        self.todo_list = TodoList()
        self.root = root
        self.root.title("Todo List App")

        # Entry for adding task
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Buttons
        tk.Button(root, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(root, text="Remove Task", command=self.remove_task).pack(pady=5)
        tk.Button(root, text="Mark Completed", command=self.mark_completed).pack(pady=5)

        # Listbox for tasks
        self.listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        self.load_listbox()

    def load_listbox(self):
        self.listbox.delete(0, tk.END)
        for t in self.todo_list.tasks:
            status = "✔️" if t["completed"] else "❌"
            self.listbox.insert(tk.END, f"{t['task']} [{status}]")

    def add_task(self):
        task = self.task_entry.get()
        if self.todo_list.add_task(task):
            self.load_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.todo_list.remove_task(index)
            self.load_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to remove!")

    def mark_completed(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.todo_list.mark_completed(index)
            self.load_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to mark completed!")



root = tk.Tk()
app = TodoApp(root)
root.mainloop()


