#!/usr/bin/env python3
import todoist_api_python.api as todoist
import datetime, threading, os

key = os.environ.get('todoist.env')
api = todoist.TodoistAPI(key)

# Get today's date in the format "YYYY-MM-DD"
today = datetime.datetime.today().strftime("%Y-%m-%d")
tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
project_id_list = []

# # Get list of all projects
# project_list = api.get_projects()
# # Print all elements of project_list as 'name, id' until i.name contains 'Dummy'
# for i in project_list:
#     print(i.id) if 'Dummy' not in i.name else None

def hyperscheduler(date):
    global findItems
    global api
    global due_today_list
    global due_today_list_id

    due_today_list = []
    due_today_list_id = []
    
    with open('/home/aarjav/Documents/Todoist Hyperscheduler/projects.txt', 'r') as f:
        # Append each line from projects.txt to project_id_list
        for line in f:
            project_id_list.append(line.strip()) if line.strip() != "" else None
            

    def findItems(i):
        global due_today_list
        global due_today_list_id
        global ch

        tasks_today = api.get_tasks(project_id=i, filter="due:today") if ch == '1' else api.get_tasks(project_id=i, filter="due:tomorrow")

        # Find position of the project id in the project_id_list and create a new list of items
        for item in tasks_today:
            due_today_list.append(item.content)
            due_today_list_id.append(item.id)

    # Run the findItems function for each project id in the list using multithreading
    threads = []
    for i in project_id_list:
        t = threading.Thread(target=findItems, args=(i,))
        threads.append(t)
        t.start()
    
    # Wait for all threads to finish
    for t in threads:
        t.join()

    print()
    print(str(len(due_today_list)) + " tasks due today.")
    print()
    
    # Set the due date as 6am
    due = datetime.datetime.strptime(date + "T06:00:00", "%Y-%m-%dT%H:%M:%S")
    # Add time difference to due date
    
    for i in due_today_list:
        # List each task and ask for how many minutes it'd take to complete
        print(f"{i}")
        cont = False
        while True:
            try:
                minutes = input("Enter the number of minutes it would take to complete: ")
                if minutes.lower() != "n":
                    minutes = int(minutes)
                    if minutes % 15 != 0:
                        print("Please enter a multiple of 15 minutes.")
                        raise ValueError
                    break
                else:
                    print()
                    cont = True
                    break
            except ValueError:
                print("Invalid input. Try again.")
        
        # Single line if statement to check if cont is True and continue to next task
        if cont:
            continue

        print(f"Start Time: {due.strftime('%H:%M')}")
        # Add minutes to title enclosed in square brackets
        title = f"{i} [{minutes}m]"

        def update_item(item_id, due, title):
            api.update_task(
                task_id=item_id,
                due_date=due.strftime("%Y-%m-%dT%H:%M:%S"),
                content=title,
            )
        # Create a new thread for each item
        t = threading.Thread(target=update_item, args=(due_today_list_id[due_today_list.index(i)], due, title))
        t.start()
        due = due + datetime.timedelta(minutes=minutes)
        print()
    
    print("Hyperscheduling complete!\n")

# Ask user if he wants to reschedule tasks due today or tomorrow
ch = input("Would you like to reschedule tasks due today(1) or tomorrow(2)? ")

if ch == "1":
    hyperscheduler(today)
elif ch == "2":
    hyperscheduler(tomorrow)

def hyperschedule(date):
    due_today_list = []
    due_today_list_id = []
    for i in project_id_list:
        for item in api.projects.get_data(i)["items"]:
            if item["due"] != None:
                if date in item["due"]["date"]:
                    # Checks if parent_id is in due_today_list_id
                    if item["parent_id"] not in due_today_list_id:
                        due_today_list.append(item["content"])
                        due_today_list_id.append(item["id"])
    for count, i in enumerate(due_today_list, start=1):
        print(f"{count}. {i}")

    print("\nNote: enter all due times without the relative date, i.e, tod or tom.\n")
    while True:
        try:
            choice = int(input("Enter the task number to reschedule: "))
            due_input = input(f"Current due date: {str(api.items.get(due_today_list_id[choice - 1])['item']['due']['date'])[11:]}\nEnter new due time for {due_today_list[choice - 1]}: ")
            
            if due_input != "":
                due = due_input
                if len(due.replace(".", ":")) == 3 or len(due.replace(".", ":")) == 4:
                    due = due.replace("am", ":00am")
                    due = due.replace("pm", ":00pm")
                # Convert from "pm" and "am" format to 24-hour format
                if "pm" in due:
                    due = due.replace(".", ":")
                    due = datetime.datetime.strptime(due, "%I:%M%p")
                    due = due.strftime("%H:%M")
                    due = datetime.datetime.strptime(due, "%H:%M")
                    due = due.strftime("%H:%M:%S")
                elif "am" in due:
                    due = due.replace(".", ":")
                    due = datetime.datetime.strptime(due, "%I:%M%p")
                    due = due.strftime("%H:%M")
                    due = datetime.datetime.strptime(due, "%H:%M")
                    due = due.strftime("%H:%M:%S")

                due = date + "T" + due
                due = {"date": due}
                api.items.update(
                    due_today_list_id[choice - 1],
                    due=due,
                )
                api.commit()
                print()
            else:
                print("No due date entered. Task not rescheduled.")
                print()
        except:
            print("\nQuitting...")
            import time
            time.sleep(1)