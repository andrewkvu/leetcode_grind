class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # arr[2 * i + 1] = 2 * arr[2 * i]
        # arr[1] = 2 * arr[2]
        # arr[3] = 2 * arr[4]
        # 0 <= i < len(arr) / 2
        
        c = Counter(arr)
        s = sorted(arr, key=lambda x: abs(x))
        # print(s) # -2, 2, -4, 4
        for num in s:
            if c[num] == 0: # can't make anymore pairs with this number? skip
                continue
            if c[2 * num] == 0: # if the current number does not have a 2 * num pair, cannot fulfill condition
                return False
            c[num] -= 1
            c[2 * num] -= 1

        return True

            
        
        
            