# hashmap realization with linked list and other
from math import log2
from tkinter.messagebox import NO


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        self.head = Node(-1)

    def insert(self, newval):
        if not self.exists(newval):
            newnode = Node(newval, self.head.next)
            self.head.next = newnode

    def delete(self, val):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, val):
        curr = self.head.next
        while curr:
            if curr.value == val:
                return True
            curr = curr.next
        return False

class MyHashSet: 
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1) >> 5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key):
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key):
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key):
        t = self.eval_hash(key)
        return key in self.arr[t]
    
class HashNode:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.size = 9973
        self.mult = 12582917
        self.data = [None for _ in range(self.size)]

    def hash(self, key):
        return key * self.mult % self.size
        
    def remove(self, key):
        hval = self.hash(key)
        node = self.data[hval]
        if not node: 
            return
        if node.key == key:
            self.data[hval] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def put(self, key, val):
        self.remove(key)
        hval = self.hash(key)
        node = HashNode(key, val, self.data[hval])
        self.data[hval] = node

    def get(self, key):
        h = self.hash(key)
        node = self.data[h]
        while node:
            if node.key == key: return node.val
            node = node.next
        return -1

mymap = MyHashMap()
mymap.remove(2)
mymap.put(3, 11)