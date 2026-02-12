class Task:
    def __init__(self,task_id,title,priority):
        self.id = task_id
        self.title = title
        self.priority = priority
        self.completed = False
        self.deleted = False


    def mark_complete(self): 
        """Mark the task as completed"""
        self.completed = True


    def mark_deleted(self):
        """Mark the task as deleted"""
        self.deleted = True

    def description(self):
        """Return a string description of the task
        """
        status = "Completed" if self.completed else "Pending"
        deleted = "Deleted" if self.deleted else ""
        return f"Task {self.id}: {self.title} | Priority: {self.priority}) | Status: {status} {deleted}"
    
    def restore(self):
        """Restore a deleted task"""
        self.deleted = False









