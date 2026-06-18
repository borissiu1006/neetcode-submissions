class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # for loop i, find all combos that has i with 2 pointers.
        nums.sort()
        output = []

        for i, a in enumerate(nums): # No negatives >> cant += 0
            if a > 0:
                break
        
            if i > 0 and a == nums[i - 1]: # Skip dup, already found all combos from a
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sums = nums[l] + nums[r] + a
                if sums == 0:
                    output.append([nums[l], nums[r], a])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # Skip dup for l, r
                        l += 1

                elif sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1

        return output
        
