class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=sorted(list(set(nums)))
        if len(n)>2:
            return n[-3]
        return n[-1]