class Solution:
    def calculate(self, s: str) -> int:    
        def update(v, op):            
            if op == '+':
                stack.append(v)
            elif op == '-':
                stack.append(-v)
        i, num, stack, sign = 0, 0, [], '+'
        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] == '(':
                num, j = self.calculate(s[i+1:])
                i += j
            elif s[i] in '+-':
                update(num, sign)
                num, sign = 0, s[i]
            elif s[i] == ')':
                update(num, sign)
                return sum(stack), i+1
            i += 1
        update(num, sign)
        return sum(stack)
