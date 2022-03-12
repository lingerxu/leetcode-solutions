# python solution for leetcode problem Rotate Array
nums = [1,2,3,4,3,1,2]
single_sets = set()

for num in nums:
    if num not in single_sets:
        single_sets.add(num)
    else:
        single_sets.remove(num)

res = single_sets.pop()

print(res)