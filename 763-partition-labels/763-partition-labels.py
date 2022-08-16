class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        res = []

        for i, char in enumerate(s):
            last[char] = i  # gets the last occurrence of each char in the string

        right = left = 0
        for i, char in enumerate(s):
            right = max(right, last[char]) # sets right to the largest window possible
            # i and right is the boundary between current char and the last occ of this char
            if i == right: # i == right means we've gotten all characters within the partition that have all the first and last occurrences inside
                res.append(1 + right - left) # append the window-size
                left = i + 1 # move base of window over for new window

        return res