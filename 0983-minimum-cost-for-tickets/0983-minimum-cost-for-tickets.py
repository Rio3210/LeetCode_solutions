class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo={}
        maxx=max(days)
        check=set(days)
        def helper(day):
            if day>maxx:
                return 0
            if day in memo:
                return memo[day]
            if day in check:
                memo[day]=min(helper(day+1)+costs[0],helper(day+7)+costs[1],helper(day+30)+costs[2])
            else:
                memo[day]=helper(day+1)
            return memo[day]
        return helper(1)