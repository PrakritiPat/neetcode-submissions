class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens: 
            if (t == '+' or t == '-' or t == '*' or t == '/'):

                operant2 = stack.pop()
                operant1 = stack.pop()
                if t == '+':
                    expression = operant1 + operant2
                elif t == '-':
                    expression = operant1 - operant2
                elif t == '*':
                    expression = operant1 * operant2
                else:
                    expression = int(operant1 / operant2)
                stack.append(expression)
            else:
                stack.append(int(t))
                
           
        ans = stack.pop()
        return ans


       
         











        