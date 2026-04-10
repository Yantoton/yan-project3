from datetime import datetime

def todo():
    todo_list = []
    while True:
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(current_time)

        banner = "Welcome to t(o_d)o list:"
        print(banner)
        choice = input("Would you like to add a task?(yes/no)")
        try:
            if choice == "yes":
                add_task = input("write here to add a task:")
                todo_list.append(add_task)
                print(f"Task {add_task} added successfully:")

            elif choice == "no":
                print("\nHere your task list is:", todo_list)
                for index, task in enumerate(todo_list, start=1):
                    print(f"{index}. {task}")
                    print("Goodbye!")
                break

            else:
                print("please enter 'yes' or 'no'")

            with open("todo.txt", "a") as file:
             file.write(f"\nToday :{current_time}"
                       f"\nTo_do task list:{todo_list} ")
        except Exception as e:
            print("Error Occured:", e)
        else:
            print("Task list saved successfully in file")
if __name__ == "__main__":
   todo()
