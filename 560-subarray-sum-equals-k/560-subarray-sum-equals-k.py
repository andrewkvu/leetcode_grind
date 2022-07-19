class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        N = len(nums)
        # presum computation
        for i in range(1, N):
            nums[i] += nums[i - 1]

        print(nums)
        # frequencies of the sums that you'll have
        counter = Counter()
        counter[0] = 1
        for num in nums:
            if num - k in counter: # num - k in counter means that num + (val in counter) = k -> increment res
                res += counter[num - k] # increment res by how many times num - k (val in counter) is in the counter at the time
            counter[num] += 1 # increase frequency of that number
        return res
        
        