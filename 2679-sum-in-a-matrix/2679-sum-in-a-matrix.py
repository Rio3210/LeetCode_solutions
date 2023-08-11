class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        nnm= [sorted(sublist) for sublist in nums]
        score=0
        
        for column in zip(*nnm):
            max_value = max(column)
            score += max_value

        return score
                
            