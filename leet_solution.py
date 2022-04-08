class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        result = 0
        arr.sort()
        n = len(arr)
        
        for i in range(n):
            subt = target - arr[i]
            j = i + 1
            k = len(arr) - 1
            
            while j < k:
                if arr[j] + arr[k] < subt:
                    j += 1
                elif arr[j] + arr[k] > subt:
                    k -= 1
                # when == subt
                elif arr[j] != arr[k]: 
                    left = 1
                    right = 1
                    while j + 1 < k and arr[j] == arr[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k-1]:
                        right += 1
                        k -= 1
                    result += left * right
                    result %= MOD
                    j += 1
                    k -= 1
                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    result += (k-j+1) * (k-j) / 2
                    result %= MOD
                    break
            
        return result

    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # logic is finding the largest two, then 
        def remove_largest():
            index_of_largest = stones.index(max(stones))
            # Swap the stone to be removed with the end.
            stones[index_of_largest], stones[-1] = stones[-1], stones[index_of_largest]
            return stones.pop()

        while len(stones) > 1:
            stone1 = remove_largest()
            stone2 = remove_largest()
            if stone1 != stone2:
                stones.append(stone1 - stone2)

        return stones[0] if stones else 0




sol = Solution()
stones = [10,4,2,10]

result = sol.lastStoneWeight(stones)
print(result)