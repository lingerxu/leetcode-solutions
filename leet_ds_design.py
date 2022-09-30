class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.myqueue = [None] * k
        self.idx_front = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count == self.capacity:
            return False
        self.myqueue[(self.idx_front + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.count == 0:
            return False
        self.idx_front = (self.idx_front + 1) % self.capacity
        self.count -= 1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.myqueue[self.idx_front]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.myqueue[(self.idx_front + self.count - 1) % self.capacity]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.capacity
        

    def print(self):
        """
        :rtype: bool
        """
        print(self.myqueue[self.idx_front:(self.idx_front + self.count) % self.capacity])
        


# Your MyCircularQueue object will be instantiated and called as such:
k = 10
obj = MyCircularQueue(k)
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_1 = obj.enQueue(4)
obj.print()
param_4 = obj.Rear()
print(param_4)
print(obj.isFull())
param_5 = obj.deQueue()
obj.print()
param_6 = obj.enQueue(5)
param_7 = obj.Rear()
print(param_7)
obj.print()