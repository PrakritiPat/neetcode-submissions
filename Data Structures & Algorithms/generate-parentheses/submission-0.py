class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(opened,closed):
            
            if len(path) == 2*n:
                res.append("".join(path))
                return 

            if opened > closed: 
                path.append(')')
                backtrack(opened,closed +1)
                path.pop()

            if opened < n: 
                path.append('(')
                backtrack(opened + 1 ,closed)
                path.pop()


        backtrack(0,0)
        return res

            


        