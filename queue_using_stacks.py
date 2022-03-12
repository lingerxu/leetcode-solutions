# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue(object):
    def __init__(self):
        self.instack = []
        self.outstack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.instack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.move()
        return self.outstack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outstack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.instack) and (not self.outstack)

    def move(self):
        """
        This is a helper function that moves all the current instack elements to outstack when needed
        """
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.empty())