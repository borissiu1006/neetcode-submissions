class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        # exclude ifself from product
        for i in range(len(nums)):
            no_i = nums.copy()
            del no_i[i]

            product = 1
            for n in no_i:
                product *= n
            output.append(product)

        return output

            


        