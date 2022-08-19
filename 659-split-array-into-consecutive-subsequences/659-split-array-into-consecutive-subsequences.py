class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        have = Counter(nums)
        seqEnd = Counter()
        
        # basically have the two ways to add onto or create a sequence
        # then keep track of where the sequence ends in another counter
        # if you can't do either of these, the array can't be split 
        for num in nums:
            if have[num] == 0:
                continue
            have[num] -= 1
            # if there is a sequence that ends in the number 1 before this one, you can extend the sequence
            if seqEnd[num - 1] > 0:
                seqEnd[num - 1] -= 1
                seqEnd[num] += 1
            # you can also create a sequence of 3 if you still have the values for the numbers 1 and 2 after this one
            # since problem specifically asks for consecutive increasing sequence
            elif have[num + 1] > 0 and have[num + 2] > 0:
                have[num + 1] -= 1
                have[num + 2] -= 1
                seqEnd[num + 2] += 1
            else:
                return False
        return True
                