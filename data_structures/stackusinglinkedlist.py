class Node:
    def __init__(self, priority, job):
        self.nextNode = None
        self.priority = priority
        self.job = job

    def getPriority(self):
        return self.priority

    def getJob(self):
        return self.job

    def setPriority(self, priority):
        self.priority = priority

    def setJob(self, job):
        self.job = job

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, priority, job):
        newnode = Node(priority, job)
        if self.head is None:
            self.head = newnode
        else:
            newnode.nextNode = self.head
            self.head = newnode

    def count(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.nextNode
        return count

    def displayjobs(self):
        curr = self.head
        dict_of_jobs = {}
        while curr is not None:
            dict_of_jobs[curr.getPriority()] = curr.getJob()
            curr = curr.nextNode
        order_of_jobs = list(dict_of_jobs.keys())
        order_of_jobs.sort(key=int)
        for order in order_of_jobs:
            print(dict_of_jobs[order])
        print('Total jobs:', self.count())

class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, priority, job):
        self.insert(priority, job)

    def pop(self):
        if self.head is None:
            return None
        job = self.head.getJob()
        self.head = self.head.nextNode
        return job

    def displayjobs(self):
        curr = self.head
        while curr is not None:
            print(self.pop())
            curr = curr.nextNode

class PriorityList(Stack):
    def __init__(self):
        super().__init__()

    def insert(self, priority, job):
        newnode = Node(priority, job)
        if self.head is None or self.head.getPriority() > priority:
            newnode.nextNode = self.head
            self.head = newnode
        else:
            curr = self.head
            prev = None
            while curr is not None and curr.getPriority() <= priority:
                prev = curr
                curr = curr.nextNode
            newnode.nextNode = curr
            prev.nextNode = newnode

    def displayjobs(self):
        curr = self.head
        while curr is not None:
            print(f"Priority: {curr.getPriority()}, Job: {curr.getJob()}")
            curr = curr.nextNode
        print('Total jobs:', self.count())

# Test Cases
if __name__ == "__main__":
    # Using PriorityList
    pl = PriorityList()
    pl.insert(2, 'Schedule date for first meeting')
    pl.insert(1, 'Delegate tasks to members')
    pl.insert(3, 'Plan project schedule')
    
    print("Jobs in Priority Order:")
    pl.displayjobs()  # Should display jobs in order of priority

    # Using Stack
    ss = Stack()
    ss.push(2, 'Schedule date for first meeting')
    ss.push(1, 'Delegate tasks to members')
    ss.push(3, 'Plan project schedule')
    
    print("\nJobs from Stack:")
    ss.displayjobs()  # Should pop and display jobs in reverse order of insertion
