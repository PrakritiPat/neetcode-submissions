class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        answer_stack = []
        for n in range(len(tokens)):
            if tokens[n] not in ['+', '-', '*', '/']:
                answer_stack.append(int(tokens[n]))
        

        
            if (tokens[n] == '+'):
                operator_2 = answer_stack.pop()
                operator_1 = answer_stack.pop()
                new_value = operator_1 + operator_2
                answer_stack.append(new_value)
            if (tokens[n] == '-'):
                operator_2 = answer_stack.pop()
                operator_1 = answer_stack.pop()
                new_value = operator_1 - operator_2
                answer_stack.append(new_value)
            if (tokens[n] == '*'):
                operator_2 = answer_stack.pop()
                operator_1 = answer_stack.pop()
                new_value = operator_1 * operator_2
                answer_stack.append(new_value)
            if(tokens[n] == '/'):
                operator_2 = answer_stack.pop()
                operator_1 = answer_stack.pop()
                new_value = operator_1 / operator_2
                answer_stack.append(int(new_value))
           

        answer = answer_stack.pop()
        return answer












        