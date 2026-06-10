class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0
        if len(nums1) == 0 or len(nums2) == 0:
            return []
            
        while l != len(nums1):
            if nums1[l] == 0 and m == 0:
                nums1[l] = nums2[r]
                l, r = l+1, r+1
            else:
                l += 1
                m -= 1

        return nums1.sort()