class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacency list, list of all prerequisites
        courseMap = {i: [] for i in range(numCourses)}

        # map all prerequisites
        for take, prereq in prerequisites:
            courseMap[take].append(prereq)

        # set for all courses seen so far along DFS path
        courseSeen = set()

        def dfs(course):
            if course in courseSeen: # base case: loop detection
                return False
            if courseMap[course] == []: # no prereqs: can take course
                return True

            courseSeen.add(course)
            for prereq in courseMap[course]:
                if not dfs(prereq): # don't have to go through all the other ones if one prereq is bad
                    return False
            courseSeen.remove(course)
            courseMap[course] = [] # empty list means it's gone through all the checks and is good
            return True
        # print(courseMap)

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True