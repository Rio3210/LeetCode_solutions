class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return map(list, itertools.permutations(nums))