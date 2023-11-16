class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        ca=capacityA
        cb=capacityB
        left=0
        right=len(plants)-1
        count=0
        while left<=right:
            if left==right:
                if ca>=cb:
                    if plants[left]>ca:
                        count+=1
                    return count
                else:
                    if plants[right]>cb:
                        count+=1
                    return count
            if plants[left]>ca:
                ca=capacityA
                count+=1
            if plants[right]>cb:
                cb=capacityB
                count+=1
            
            ca-=plants[left]
            cb-=plants[right]
            left+=1
            right-=1
            
        return count
                        