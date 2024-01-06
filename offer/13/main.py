class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = []
        
        def get_count(x: int):
            r = 0
            while k:
                r+=k%10
                k=k//10
            return r
        
        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n or get_count(i)+get_count(j)>k or (i,j) in visited:
                return 0
            
            visited.append((i,j))
            
            return 1 + dfs(i+1,j) + dfs(i,j+1)
        
        return dfs(0,0)
            