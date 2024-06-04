tasks=[]

while True:
    user_action= input("Please choose action (add, remove, view or exit): ")
    if user_action == "add":
        tasks.append(input("please add a task: "))
        print("task added")
    elif user_action == "remove":
        if not tasks:
            print("no tasks to remove")
        else:
            task = input("please choose task: ")
            if task in tasks:
                tasks.remove(task)
                print("task removed")
            else:
                print("task not found")
    elif user_action =="view":
        if not tasks:
            print("no tasks to view")
        else :
            for task in tasks:
                print(task)
    elif user_action == "exit":
        break
    else :
        print("invalid action")