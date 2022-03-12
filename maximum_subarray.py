nums = [-2,1,-3,4,-1,2,1,-5,4]
        
current_sum = 0
max_value = -10**4

for i, val in enumerate(nums):
    current_sum += val
    if max_value < current_sum:
        max_value = current_sum
    if current_sum < 0:
        current_sum = 0
        
print(max_value)
        
"""
# the recursive solution - like, what's the point???
    
def max_subarray_recur(self, nums, left, right):
    if right == left:
        return nums[left]

    middle = int((left+right) / 2)
    #print(f"middle is {middle}")
    left_ans = self.max_subarray_recur(nums, left, middle)
    #print(f"left answer is {left_ans}")
    right_ans = self.max_subarray_recur(nums, middle+1, right)
    #print(f"right answer is {right_ans}")
    left_max = nums[middle]
    right_max = nums[middle+1]
    tmp = 0
    for i in range(middle, left-1, -1):
        tmp += nums[i]
        if tmp > left_max:
            left_max = tmp

    tmp = 0
    for i in range(middle+1, right+1):
        tmp += nums[i]
        if tmp > right_max:
            right_max = tmp
    #print(f"left max is {left_max}, right max is {right_max}, their sum is {left_max+right_max}")

    return max(max(left_ans, right_ans), left_max+right_max)
    

    nums_len = len(nums)
    if nums_len < 1:
        mnax_value = 0
    else:
        max_value = self.max_subarray_recur(nums, 0, nums_len-1)
        
    return max_value

"""