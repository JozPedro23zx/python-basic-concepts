from tasks import *

def main():
    print("Welcome to the Task Control")

    while True:
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Calculate deadline")
        print("6. Exit")

        option = input("Select option: ").strip()

        if option == "1":
            addTask()
        elif option == "2":
            listTask()
        elif option == "3":
            updateTask()
        elif option == "4":
            deleteTask()
        elif option == "5":
            calculate_days()
        elif option == "6":
            print("Shut down program.") 
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
