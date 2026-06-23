class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = curSum = 0
        minlength = float('inf')

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target: # Keep shrinking
                minlength = min(r - l + 1, minlength)
                curSum -= nums[l]
                l += 1


        if minlength != float('inf'):
            return minlength
        else:
            return 0