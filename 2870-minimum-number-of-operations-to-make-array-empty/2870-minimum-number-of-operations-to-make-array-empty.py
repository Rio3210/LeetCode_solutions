class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for num in count:
            while count[num]!=0 :
                if count[num]%3==0:
                    ans+=1
                    count[num]=count[num] - 3
                    
                elif count[num]%2==0:
                    ans+=1
                    count[num]=count[num] - 2
                elif (count[num]-3) % 2==0 and count[num]>1:
                    ans+=1
                    count[num]=count[num] - 3
                
                elif (count[num]-2) % 3==0 and count[num]>1:
                    ans+=1
                    count[num]=count[num] - 2
                
                else:
                    break
        if any(count.values()):
            return -1
        else:
            return ans        
        