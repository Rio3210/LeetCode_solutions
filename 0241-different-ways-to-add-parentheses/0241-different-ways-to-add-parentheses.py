class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache
        def helper(expr):
            if expr.isdigit():
                return [int(expr)]
            
            results = []
            for i in range(len(expr)):
                if expr[i] in '+-*':
                    left_results = helper(expr[:i])
                    right_results = helper(expr[i+1:])
                    
                    for left in left_results:
                        for right in right_results:
                            if expr[i] == '+':
                                results.append(left + right)
                            elif expr[i] == '-':
                                results.append(left - right)
                            elif expr[i] == '*':
                                results.append(left * right)
            
            return results
        
        ans = helper(expression)
        return ans