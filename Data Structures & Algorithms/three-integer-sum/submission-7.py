class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # try k = len(nums) - 1
        # for each time, try two pointers i, j in numbers[:k]
        i, j, k = 0, len(nums) - 2, len(nums) - 1
        nums.sort()
        output = []

        for i, a in enumerate(nums):
            if a > 0:
                break
        
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sums = nums[l] + nums[r] + a
                if sums == 0:
                    output.append([nums[l], nums[r], a])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1

        return output
        
