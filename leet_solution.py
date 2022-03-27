class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # vertical sort
        # so my sorting logic is to go through 0-nth bit from 0-mth row
        # to put all rows with 0 before rows with 1 at the ith bit
        # my initial list would be [0, 1, 2, ..., m]
        # for every row with 0 at ith bit, move the row index to the front - at the end of all 0s
        m = len(mat)
        n = len(mat[0]) # because 2 <= n, m, so no edge cases here
        result = list(range(m))
        num_zeroes = 0
        for colidx in range(0, n):
            for rowidx in range(num_zeroes, m):
                if mat[rowidx][colidx] == 0:
                    # take rowidx out of result and insert it back to result
                    tmpidx = result[rowidx]
                    result.remove(tmpidx)
                    result.insert(num_zeroes, tmpidx)
                    # sort the mat as well
                    row = mat.pop(rowidx)
                    mat.insert(num_zeroes, row)
                    num_zeroes += 1

        return result[:k]


        

sol = Solution()
mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2

result = sol.kWeakestRows(mat, k)
print(result)