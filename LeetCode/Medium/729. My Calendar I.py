class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calender:
            if end > s and start < e:
                return False
        self.calender.append([start,end])
        return True


############################
# BST (Binary Search Tree)
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
    
    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        return False
        

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root == None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))
                

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
obj = MyCalendar()
print(obj.book(10,20))

