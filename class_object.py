import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        print(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# k = 3
# nums = [4, 5, 8, 2]
# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
param_1 = obj.add(3)
print(param_1)
# param_1 = obj.add(5)
# print(param_1)
# param_1 = obj.add(10)
# print(param_1)
# param_1 = obj.add(9)
# print(param_1)
# param_1 = obj.add(4)
# print(param_1)