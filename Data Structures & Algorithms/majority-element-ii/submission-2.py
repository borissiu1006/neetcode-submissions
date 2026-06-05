class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = set() # no duplicates
        checker = {}

        for i in nums:
            if i not in checker:
                checker[i] = 1
            else:
                checker[i] += 1

            if checker[i] > len(nums) / 3 and i not in output:
                output.add(i)

        return list(output)