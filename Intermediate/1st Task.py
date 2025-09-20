import csv
import os
task_file='task.csv'
def load_tasks():
  tasks=[]
  if os.path.exists(task_file):
    with open(task_file, 'r', newline='') as file:
      reader=csv.DictReader(file)
      for row in reader:
        tasks.append({"Description":row['Description'], "Completed":row['Completed']=='True'})
  return tasks
        
def save_tasks(tasks):
  with open(task_file,'w', newline='')as file:
    fieldnames=["Description","Completed"]
    writer=csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for task in tasks:
      writer.writerow({"Description":task["Description"], "Completed":task["Completed"]})

def add_tasks():
  no_of_tasks=int(input("Enter No. of Tasks you want to Input: "))
  try:
    no_of_tasks = int(input("Enter No. of Tasks you want to Input: "))
  except ValueError:
    print("Please enter a valid number.")
    return
  for i in range(no_of_tasks):
    tasks=load_tasks()
    description=input(f"Enter task {i+1} description: ")
    tasks.append({"Description":description, "Completed":False})
    save_tasks(tasks)
    print("Your task is added successfully.")
  
def view_tasks():
  tasks=load_tasks()
  if not tasks:
    print("No task was found in the List.")
  else:
    for index, task in enumerate(tasks, start=1):
      status="Completed" if task['Completed'] else "Not Completed"
      print(f"{index}.[{status}] {task['Description']}")

def delete_tasks(task_number):
  tasks=load_tasks() 
  if 1<=task_number<=len(tasks):
     removed=tasks.pop(task_number-1)
     save_tasks(tasks)
     print(f"Deleted Task: {removed['Description']}")
  else:
     print("The provided task number is invalid.")

def mark_task_done(task_number):
  tasks=load_tasks()
  if 1<=task_number<=len(tasks):
    tasks[task_number-1]['Completed']=True
    save_tasks(tasks)
    print("The task is marked as Completed.")
  else:
    print("The provided task number is invalid.")

def mark_task_undone(task_number):
  tasks=load_tasks()
  if 1<=task_number<=len(tasks):
    tasks[task_number-1]['Completed']=False
    save_tasks(tasks)
    print("The task is marked as Not Completed.")
  else:
    print("The provided task number is invalid.")

def to_do_list():
  while True:
    print("\n=== To-Do List Menu ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Mark Task as Not Completed")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_tasks()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_number = int(input("Enter task number to delete: "))
        delete_tasks(task_number)
    elif choice == '4':
        task_number = int(input("Enter task number to mark as done: "))
        mark_task_done(task_number)
    elif choice == '5':
        task_number = int(input("Enter task number to mark as not done: "))
        mark_task_undone(task_number)
    elif choice == '6':
        print("Exiting the To-Do List.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

to_do_list()