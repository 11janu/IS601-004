from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    # include task,last activity date and time()
    task['lastActivity'] = datetime.now()
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    try:
        task['due'] = str_to_datetime(due)
        task['name'] = name
        task['description'] = description
    except:
        print("Task could not be added because some data is missing or due date is in the wrong format")
        return
    # add the new task to the tasks list
    tasks.append(task)
    # output a message confirming the new task was added or if the addition was rejected due to missing data
    print("Task added successfully")
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My ucid:js2679, date:02/23/23
    # Solution Summary

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    try:
        task = tasks[index-1]
    except IndexError:
        print("Invalid index, task not updated.")
        return
    
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    
    # Prompt user to update name and show the existing value if it exists
    name_input = input(f"What's the name of this task? (TODO name) (Current: {task['name']})\n").strip()
    name = name_input or task['name']
    
    # Prompt user to update description and show the existing value if it exists
    input_desc = input(f"What's a brief descriptions of this task? (TODO description) (Current: {task['description']})\n").strip() 
    desc = input_desc or  task['description']
    
    # Prompt user to update due date and show the existing value if it exists
    try:
        task['due'] = datetime.strptime(str(task['due']), '%Y-%m-%d %H:%M:%S')

        due_str = task['due'].strftime('%m/%d/%y %H:%M:%S') if task['due'] else None
    except:
        due_str = task['due'].strftime('%Y-%m-%d %H:%M:%S') if task['due'] else None
        
    due_input = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) (Current: {due_str})\n").strip()
    due = str_to_datetime(due_input) if due_input else task['due']
    
    print("Check",len(name_input),len(due_str),len(input_desc),name_input,input_desc,due)
    
    if len(name_input) != 0 or len(input_desc) != 0 or len(due_input) != 0 :
        update_task(index, name=name, description=desc, due=due)
    else:
        print("Task not updated as no new data was provided.")
    
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My ucid:js2679, date:02/23/23
    # Solution Summary
    # Accessed the task by indexing.I have accesed the existing property of each TODos from the task and shown them by using string formatting.


def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index

    try:
        task = tasks[index-1]
    except IndexError:
        print("Invalid index, task not updated.")
        return
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    if name is not None:
        task['name'] = name
    if description is not None:
        task['description'] = description
    if due is not None:
        task['due'] = str_to_datetime(str(due))
    # update lastActivity with the current datetime value.
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    if name is not None or description is not None or due is not None :
        task['lastActivity'] = datetime.now()
        print("Task updated successfully.")
    else:
        print("Task not updated as no new data was provided.")
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My UCID is js2679 and the date is 02/23/23
    # Solution Summary

    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        task = tasks[index-1]
    except IndexError:
        print("Invalid index, task not updated.")
        return
    # If it's not done, record the current datetime as the value
    if not task['done']:
        task['done'] = datetime.now()
        print(f"Task {index + 1} marked as done successfully at {task['done']}")
    # If it is done, print a message saying it's already completed
    else:
        print(f"Task {index + 1} is already marked as done")
    # make sure save() is still called last in this function
    save()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My ucid:js2679, date:02/23/23
    # Solution Summary:

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    task = {}
    try:
        task = tasks[index-1]
    except IndexError:
        print("Invalid index, task not updated.")
        return
    # utilize the given print statement when a task is found
    print(f"Name: {task['name']}")
    print(f"Description: {task['description']}")
    print(f"Due: {task['due']}")
    print(f"Completed: {'Yes' if task['done'] else 'No'}")
    print(f"Last Activity: {task['lastActivity']}")
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My ucid:js2679 , date: 02/23/23
    # Solution Summary:


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        task = tasks.pop(index - 1)
        print(f"Task '{task['name']}' deleted successfully")
    except IndexError:
        print(f"Invalid index, no task deleted")
        return
    # make sure save() is still called last in this function

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    _tasks = [task for task in tasks if not task['done']]
    list_tasks(_tasks)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My ucid: js2679, date: 02/23/23
    # Solution Summary:
def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    _tasks = []
    
    now = datetime.now()
    # loop through all tasks
    for task in tasks:
        if not task['done'] and task['due']:
            due_date = str_to_datetime(str(task['due']))
            if now > due_date:
                _tasks.append(task)
    # pass that list into list_tasks()
    list_tasks(_tasks)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My ucid:js2679, date:02/23/23
    # Solution Summary:
    

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    task = {}
    try:
        task = tasks[index-1]
    except IndexError:
        print("Invalid index, task not found.")
        return
    # get the days, hours, minutes, seconds between the due date and now
    now = datetime.now()
    due = str_to_datetime(str(task["due"]))
    if due is None:
        print("Task has no due date.")
        return

    if now > due:
        # calculate overdue time
        time_diff = now - due
        time_str = f" overdue {time_diff.days} days, {time_diff.seconds // 3600} hours, {(time_diff.seconds % 3600) // 60} minutes, {time_diff.seconds % 60} seconds"
    else:
        # calculate remaining time
        time_diff = due - now
        time_str = f" remaining {time_diff.days} days, {time_diff.seconds // 3600} hours, {(time_diff.seconds % 3600) // 60} minutes, {time_diff.seconds % 60} seconds remaining"
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    print(f"Time remaining for {task['name']}: {time_str}")
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # UCID:js2679 , Date:02/23/23
    # Solution Summary


# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()