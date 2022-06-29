class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sorts first index by small value and second value normal
        # x is each individual array of length 2
        # so -x[0] would be reversed biggest to smallest 2 5 6 8 -> -8 -6 -5 -2
        # prioritizes 0th index biggest to smallest, then if 0th indices are equal
        # uses the 1st index to sort
        people.sort(key = lambda x: (-x[0], x[1]))
        # print(people) # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]

        res = []

        for person in people:
            # inserts person at person[1] index
            res.insert(person[1], person)
        return res