tasks=[]
def add_tasks():
    task=input("Enter a new task: ")
    tasks.append(task)
    print("\nTask added Successfully.")

def delete_tasks():
    if len(tasks)==0:
        print("No Tasks to Delete.")
    else:
        print("Tasks:")
        for i,task in enumerate(tasks):
            print(f"{i+1}.{task}")
        choice=int(input("Enter the task number to delete: "))
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task deleted Successfully.")
        else:
            print("Invalid Task Number.")

def view_tasks():
    if len(tasks)==0:
        print("No Tasks.")
    else:
        print("List of Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")

def main():
    while True:
        print("\nTo-Do-List Application")
        print("1.Add Task")
        print("2.View Task")
        print("3.Delete Task")
        print("4.Quit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            add_tasks()
        elif choice==2:
            view_tasks()
        elif choice==3:
            delete_tasks()
        elif choice==4:
            print("Exited from the To-Do-List.")
            break
        else:
            print("Invalid choice,please enter correct choice: ")

if __name__=="__main__":
    main()
