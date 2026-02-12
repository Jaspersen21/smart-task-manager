from task import Task
from task_manager import TaskManager

# Create a new task
task1 = Task(1, "Submit report", 3)
print(task1.description())  # Should print task details with status "Pending"

# Print initial completed state
print(task1.completed)  # Should print False

# Mark the task complete
task1.mark_complete()

# Print new state
print(task1.completed)  # Should print True


task1.mark_deleted()
print(task1.deleted)  # Should print True

# Create a TaskManager and add tasks
manager = TaskManager()

manager.add_task("Submit report", 3)
manager.add_task("Prepare presentation", 2) 
manager.add_task("Email client", 1)  

print("All tasks:")
manager.list_tasks()

print("\nAfter deletion:")
manager.delete_task(2)
manager.list_tasks()

print("\nAfter undo:")
manager.undelete_task()
manager.list_tasks()

print("\nNext task to do:")
next_task = manager.get_next_task()
if next_task:
    print(next_task.title, next_task.priority) # Should print "Email client" with priority 1 else: print("No tasks available")
    
