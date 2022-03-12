nums = [0]
indexes_nonzero = []
len_nonzeros = 0
len_nums = len(nums)

for i, val in enumerate(nums):
    if val != 0:
        indexes_nonzero.append(i)
        len_nonzeros += 1

num_idx = 0
while num_idx < len_nums:
    if num_idx < len_nonzeros:
        nums[num_idx] = nums[indexes_nonzero[num_idx]]
    else:
        nums[num_idx] = 0
    num_idx += 1

print(nums)
