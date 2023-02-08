class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        nmm=skill[0]+skill[len(skill)-1]
        ans=0
        for i in range(int(len(skill)/2)):
            if skill[i]+skill[len(skill)-1-i]!=nmm:
                return -1
            
            ans+=skill[i]*skill[len(skill)-1-i]
        return ans
            
        
        
                
            