class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # for loop to iterate through all possible integers
        # check if 3 and 5 first
        # then check div by 3
        # then check div by 5
        # else append "i"
        res = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        
        return res