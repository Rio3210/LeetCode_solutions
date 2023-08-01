class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1:
            return 1
        b = [digit % 1337 for digit in b]
        def recur(x, n):
            if n == 0:
                return 1
            y = recur(x, n // 2)
            y = (y * y) % 1337
            if n % 2 == 1:
                y = (y * x) % 1337
            return y
        res = 1
        for digit in b:
            res = recur(res, 10) # split b into chunks of length 1
            res = (res * recur(a, digit)) % 1337
        return res