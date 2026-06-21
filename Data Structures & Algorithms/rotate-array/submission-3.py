class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        # Reverse
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        
        reverse(0, n - 1)
        reverse(0, k  - 1)
        reverse(k, n - 1)

        '''
        # Cyclesort
        count = start = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                nexti = (current + k) % n
                nums[nexti], prev = prev, nums[nexti]
                
                current = nexti
                count += 1
                if start == current:
                    break
            start += 1
        '''
        '''
        # Slicing: Not real O(1) extra space

        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
        '''
        