from task import Task
import heapq
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.tasks_by_id = {}
        self.history_stack = []
        self.next_id = 1
        self.priority_queue = []
        

    def add_task(self,title,priority):
        task = Task(self.next_id,title,priority)
        self.tasks.append(task) 
        self.tasks_by_id[self.next_id] = task
        heapq.heappush(self.priority_queue, (priority, task.id, task))
        self.next_id += 1

    def delete_task(self,task_id):
        task = self.tasks_by_id.get(task_id)
        if task and not task.deleted:
            task.mark_deleted()
            self.history_stack.append(("delete", task))

    def complete_task(self,task_id):
        task = self.tasks_by_id.get(task_id)

        if task and not task.deleted and not task.completed:
            task.completed = True
            self.history_stack.append(("complete", task))


    def undo(self):
        if not self.history_stack:
            return

        action, task = self.history_stack.pop()
        if action == "delete":
            task.deleted = False
        elif action == "complete":
            task.completed = False                


    #def undelete_task(self):
        #if self.deleted_stack:
            # task.restore()   

    def list_tasks(self):
        for task in self.tasks:
            if not task.deleted:
                status =  "Done" if task.completed else "pending" 
                print(f"Task {task.id}: {task.title} | Priority: {task.priority} | Status: {status} ") 



    def get_next_task(self):
        while self.priority_queue:
            priority, task_id, task = self.priority_queue[0]  # peek at the top of the heap

            #skip deleted tasks
            if task.deleted:
                heapq.heappop(self.priority_queue)  # remove the deleted task
                continue
            return task
        return None  # No tasks available

                       
