class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        def dfs(r,c):
            #base case: if my grid was a singular cell, then return 1
            res = 1 
            

            if (r,c) in dp:
                return dp[(r,c)]
            
          
           

             
        #my options are: if its a valid path, meaning the value is larger than then the current cell then consider that an option, just dont know how to write it 
        # if the value is increasing then thats where the +1 will be 
            
            nr = r + 1
            nc = c
            if (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[r][c] < matrix[nr][nc]):
                res = max(res, 1+ dfs(nr,nc))

            nr = r -1
            nc = c
            if (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[r][c] < matrix[nr][nc]):
                res = max(res, 1+ dfs(nr,nc))

            nr = r 
            nc = c+1
            if (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[r][c] < matrix[nr][nc]):
                res = max(res, 1+ dfs(nr,nc))

            nr = r 
            nc = c -1
            if (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[r][c] < matrix[nr][nc]):
                res = max(res, 1+ dfs(nr,nc))
            dp[(r,c)] = res
            return res

        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])): 
                res = max(res,dfs(r,c))

        
        return res





        