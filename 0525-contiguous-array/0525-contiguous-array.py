class Solution:
	def findMaxLength(self, nums: List[int]) -> int:
		dp = {}
		dp[0] = -1
		curSum = 0
		result = 0

		for i in range(len(nums)):
			if nums[i] == 1:
				curSum += 1

			else:
				curSum -= 1

			if curSum not in dp:
				dp[curSum] = i

			else:
				result =max(result, i - dp[curSum])

		return result