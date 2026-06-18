class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        for i, iv in enumerate(nums):
            if i > 0 and iv == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                jv = nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, len(nums) - 1
                while l < r:
                    sums = iv + jv + nums[l] + nums[r]
                    if sums == target:
                        output.append([iv, jv, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                    elif sums > target:
                        r -= 1
                    elif sums < target:
                        l += 1

        return output

        