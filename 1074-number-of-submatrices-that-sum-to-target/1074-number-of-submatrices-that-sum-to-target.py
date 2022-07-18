class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        res = 0
        for row in range(M):
            for col in range(1, N):
                # prefix sum where you take the previous value and add to current
                matrix[row][col] += matrix[row][col - 1]
        
        # for each pair of columns, there's a range between them to compute the values
        for col_begin in range(N):
            for col_end in range(col_begin, N):
                freqMap = defaultdict(int)
                freqMap[0] = 1 # key is unique value of prefix sum, val is number of prefix sum value
                curSum = 0
                for r in range(M):
                    if col_begin > 0: # whole range of the column
                        curSum += matrix[r][col_end] - matrix[r][col_begin - 1]
                    else:
                        curSum += matrix[r][col_end]
                    res += freqMap[curSum - target]
                    freqMap[curSum] += 1 # increase frequency of this sum
        
        return res