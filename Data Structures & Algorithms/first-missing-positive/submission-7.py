class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n: # filter
                i += 1
                continue

            index = nums[i] - 1 # cycle sort
            if nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i] 
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
    '''
        # O(nlogn) still
        nums.sort()
        miss = 1
        for num in nums:
            if num > 0 and miss == num:
                miss += 1 # stop adding when sequence is broke >> found s.p.i
        return miss
    '''

    '''
        # O(nlogn) cuz .sort()
        nums.sort()

        # smallest pos. integer = i between num.next and num IF num.next > 1 and num.next - num > 0
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
    '''
            
            


        