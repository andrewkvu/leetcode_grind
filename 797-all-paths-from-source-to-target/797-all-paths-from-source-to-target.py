class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # adj = {}
        # for i in range(len(graph)):
        # adj[i] = graph[i]
        N = len(graph)
        res = []
        
        # need to keep track of a path that doesn't change through iterations
        # thus you somewhat need the recursive dfs part and within the function parameter
        # that way you can build upon each path in their own dfs call
        def dfs(path, vert):
            path.append(vert)
            if vert == N - 1:
                res.append(path.copy())
            for neighbor in graph[vert]:
                dfs(path, neighbor)
            path.pop()
            
        dfs([], 0)
        return res
    
    