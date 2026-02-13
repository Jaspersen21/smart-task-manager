from task import Task
import heapq
import json

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
    
    def save_to_file(self,filename):
        data = []
        for task in self.tasks:
            data.append({
                "id": task.id,
                "title": task.title,
                "priority": task.priority,
                "completed": task.completed,
                "deleted": task.deleted
            })
        with open(filename,"w") as f:
            json.dump(data,f,indent=4)



    def load_from_file(self, filename):
        with open(filename,"r") as f:
            data = json.load(f)

            #clear current tasks
            self.tasks = []
            self.tasks_by_id = {}
            self.priority_queue = []
            self.history_stack = []

            for item in data:
                task = Task(
                    item["id"],
                    item["title"],
                    item["priority"]
                )

                task.completed = item["completed"]
                task.deleted = item["deleted"]

                self.tasks.append(task)
                self.tasks_by_id[task.id] = task

                #Only push non deleted tasks to the priority queue
                if not task.deleted:
                    heapq.heappush(self.priority_queue, (task.priority, task.id, task))

            



    

                       
