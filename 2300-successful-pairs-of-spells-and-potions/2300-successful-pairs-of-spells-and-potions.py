class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        n = len(potions)
        ans = []
        for sp in spells:
            other = math.ceil(success/sp)
            j = bisect.bisect_left(potions, other)
            # print(j)
            ans.append(n - j)
        return ans
                           
                           
            