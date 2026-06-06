class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        # smallest pos. integer = i between num.next and num if num.next > 1 and num.next - num > 0
        for i in range(len(nums)):
            num = nums[i]

            # edge cases:
            if num > 1 and i == 0: # first num > 1 already
                result = 1
                return result
            elif num < 1 and i == len(nums) - 1: # all negatives
                result = 1
                return result

            try:
                num_next = nums[i + 1]
                if num_next > 1 and (num_next - num) > 1: # normal
                    if num <= 0:
                        result = 1
                        return result
                    else:
                        result = num + 1
                        return result

            except IndexError: # handle cant find s.p.i
                result = nums[i] + 1
                return result
            
            


        