class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        temp=0
        result=0
        if sum(cost)>sum(gas):
            return -1
        for i in range(len(gas)):
            temp+=gas[i]-cost[i]
            if temp<0:
                temp=0
                result=i+1
        return result
        
#         diff=[]
#         if sum(gas)>=sum(cost):
            
#             for i in range(len(gas)):
#                 diff.append(gas[i]-cost[i])
#             print(diff)
#             for i in diff:
               
#                 # if total>0:
#                 #     return i
#         else:
#             return -1