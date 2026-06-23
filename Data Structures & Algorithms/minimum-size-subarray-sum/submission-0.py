class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = curSum = 0
        minlength = 99999

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minlength = min(r - l + 1, minlength)
                curSum -= nums[l]
                l += 1


        if minlength != 99999:
            return minlength
        else:
            return 0