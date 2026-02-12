from task import Task
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.tasks_by_id = {}
        self.deleted_stack = []
        self.next_id = 1
        

    def add_task(self,title,priority):
        task = Task(self.next_id,title,priority)
        self.tasks.append(task) 
        self.tasks_by_id[self.next_id] = task
        self.next_id += 1

    def delete_task(self,task_id):
        task = self.tasks_by_id.get(task_id)
        if task and not task.deleted:
            task.mark_deleted()
            self.deleted_stack.append(task)


    def undelete_task(self):
        if self.deleted_stack:
            task = self.deleted_stack.pop()
            task.restore()   

    def list_tasks(self):
        for task in self.tasks:
            if not task.deleted:
                status =  "Done" if task.completed else "pending" 
                print(f"Task {task.id}: {task.title} | Priority: {task.priority} | Status: {status} ") 
