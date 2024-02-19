class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = ['+','-','*','/']
        for token in tokens:

            if token in operators:
                u=stack.pop()
                v=stack.pop()
                if token == '+':
                    stack.append(u+v)
                elif token == '-':
                    stack.append(v-u)
                elif token == '*':
                    stack.append(v*u)
                elif token=='/':
                    stack.append(int(v/u))

            else:
                stack.append(int(token))
        return int(stack[-1])        