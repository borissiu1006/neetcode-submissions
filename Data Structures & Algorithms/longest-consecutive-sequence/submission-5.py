class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_streak = 0

        for num in nums:
            if num - 1 not in nums:
                current = num
                streak = 1

                while current + 1 in nums:
                    current += 1
                    streak += 1

                longest_streak = max(longest_streak, streak)

        return longest_streak