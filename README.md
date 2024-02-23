# To-Do-List
 This Python script implements a simple to-do list application. It allows users to add tasks, view tasks, delete tasks, and quit the application.
Here's a description of each function:

add_tasks(): This function prompts the user to enter a new task and appends it to the tasks list. It then prints a message confirming that the task has been added successfully.

delete_tasks(): This function first checks if there are any tasks in the list. If there are no tasks, it prints a message indicating that there are no tasks to delete. If there are tasks, it prints the list of tasks with their corresponding numbers. The user is then prompted to enter the number of the task they want to delete. If the input is valid, the selected task is deleted from the tasks list, and a message confirming the deletion is printed. If the input is invalid, a message indicating that the task number is invalid is printed.

view_tasks(): This function checks if there are any tasks in the list. If there are no tasks, it prints a message indicating that there are no tasks. If there are tasks, it prints the list of tasks with their corresponding numbers.

main(): This function contains a while loop that repeatedly displays a menu of options for the user to choose from. Based on the user's choice, it calls the corresponding function (add_tasks(), view_tasks(), delete_tasks(), or exits the loop if the user chooses to quit).

The script uses a global variable tasks to store the list of tasks. When the script is run (if __name__=="__main__":), it calls the main() function to start the application.





