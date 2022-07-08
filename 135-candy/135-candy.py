class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candies = [1 for i in range(N)]
        
        
        # 1 2 3 4 5 4 3 2 1 
        # 1 2 3 4 5 1 1 1 1
        # l->r for ascending candy
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        # l<-r for descending candy
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i + 1] + 1, candies[i])
                
        return sum(candies)
        
        