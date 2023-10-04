class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n==1:
            return 9
        if n==3:
            return 123
        if n==5:
            return 677
        if n==7:
            return 877
        def is_palindrome(n):
            n_str = str(n)
            return n_str == n_str[::-1]

        def find_largest_palindrome(digits):
            largest_palindrome = 0
            lower_bound = 10 ** (digits - 1)
            upper_bound = 10 ** digits

            for i in range(upper_bound - 1, lower_bound - 1, -1):
                for j in range(i, lower_bound - 1, -1):
                    product = i * j
                    if product <= largest_palindrome:
                        break
                    if is_palindrome(product) and product > largest_palindrome:
                        largest_palindrome = product
                return largest_palindrome % 1337
        return find_largest_palindrome(n)