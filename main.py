import tkinter as tk

def add_task():
    task = entry_task.get()
    if task: 
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        pass

# Create the main window
window = tk.Tk()
window.title("TO-DO-LIST")

# Create the input field and Add button 
entry_task = tk.Entry(window, width=40)  # Changed 'window=40' to 'width=40'
entry_task.pack(pady=10)
button_add = tk.Button(window, text="Add Task", width=15, command=add_task)  # Changed 'add Task' to 'Add Task'
button_add.pack()

# Create the task list 
listbox_tasks = tk.Listbox(window, width=40)
listbox_tasks.pack(pady=10)

# Create the Delete button 
button_delete = tk.Button(window, text="Delete Task", width=15, command=delete_task)
button_delete.pack()

# Start the main event loop
window.mainloop()
