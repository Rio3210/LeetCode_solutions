class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 

        counter = Counter(nums)
        count = max(counter.values())

        track = defaultdict(list)
        for i in range(len(nums)):
            track[nums[i]].append(i)

        return min(track[t][-1]-track[t][0]+1 for t in track if counter[t] == count)


        
                