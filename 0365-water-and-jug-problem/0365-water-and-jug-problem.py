class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        visited=set()
        
        def helper(total):
            if total==targetCapacity:
                return True
            if total in visited or total<0 or total>jug1Capacity+jug2Capacity:
                return False
            visited.add(total)
            return helper(total+jug1Capacity) or helper(total-jug1Capacity) or helper(total+jug2Capacity) or helper(total-jug2Capacity)
        return helper(0)