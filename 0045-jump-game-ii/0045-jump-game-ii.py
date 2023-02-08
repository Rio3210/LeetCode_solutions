class Solution:
    def jump(self, nums: List[int]) -> int:
                                            
        ans, maxx, end = 0, 0, 0              
        
        for i, num in enumerate(nums[:-1]): 
                                           
            maxx = max(maxx, i + num)          
                                            
            if i == end:                     
                ans += 1                              
                end = maxx 

        return ans