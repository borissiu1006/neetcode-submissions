class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack
        s = []
        operations = {'+', '-', '*', '/'}

        for i in range(len(tokens)):
            if tokens[i] not in operations:
                s.append(tokens[i])

            elif tokens[i] in operations:
                b = str(s.pop())
                a = str(s.pop())
                eq = ''.join(a)
                eq += str(tokens[i])
                eq += b
                s.append(int(eval(eq)))
        
        return int(s[0])       