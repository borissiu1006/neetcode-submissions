class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == '+':
                s.append(s.pop() + s.pop())
            elif i == '-':
                b, a = s.pop(), s.pop()
                s.append(a - b)
            elif i == '*':
                s.append(s.pop() * s.pop())
            elif i == '/':
                b, a = s.pop(), s.pop()
                s.append(int(a/b))
            else:
                s.append(int(i))
        return s[0]

    '''
        # stack, eval() and building strings are slow, still O(n) tho
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
    '''      