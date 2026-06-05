class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []
        checker = {}

        for i in nums:
            if i not in checker:
                checker[i] = 1
            else:
                checker[i] += 1

        for key, value in checker.items():
            if value > (len(nums) / 3):
                output.append(key)
        
        return output

        