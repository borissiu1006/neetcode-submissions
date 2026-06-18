class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # K-sum with recursion
        nums.sort()
        output, quad = [], []

        def ksum(k, start, target):
            if k * nums[start] > target or k * nums[-1] < target: # Check if min/max k-sums are larger/smaller than target
                return

            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target:
                        output.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                return # Cut to not perform backtracking
            
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i]) # Checks all numbers that is above K=2
                ksum(k - 1, i + 1, target - nums[i])
                quad.pop() # Checks all numbers in each level 

        ksum(4, 0, target)
        return output

    '''
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
    '''

        