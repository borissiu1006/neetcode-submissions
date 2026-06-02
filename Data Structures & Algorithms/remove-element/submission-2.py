class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # !!! use a copy (dummy) when you wanna modify an list's element while running the list
        dummy = nums.copy()
        for i in dummy:
            if i == val:
                nums.remove(i)

        k = 0
        for i in nums:
            k+= 1
        return k