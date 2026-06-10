class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        l, r = 0, 0
        while l != len(nums1):
            if nums1[l] == 0 and m == 0:
                nums1[l] = nums2[r]
                l, r = l+1, r+1
            else:
                l += 1
                m -= 1

        #nums1.sort()
        '''
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
         



        

            



