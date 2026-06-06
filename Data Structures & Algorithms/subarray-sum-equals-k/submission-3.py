class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = currentsum = 0
        prefixsum = {0 : 1}

        for i in nums:
            currentsum += i
            diff = currentsum - k # currentsum - diff = k , (track from currentsum to diff) adds up to k

            output += prefixsum.get(diff, 0)
            prefixsum[currentsum] = 1 + prefixsum.get(currentsum, 0) # Prevent first registry KeyError

        return output


'''
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(n^2)
        output = 0
        for i in range(len(nums)):
            counter = 0
            l = nums[i]
            counter += l

            if counter == k:
                output += 1

            for n in range(i + 1, len(nums)): # always after i
                r = nums[n]
                counter += r

                if counter == k:
                    output += 1

        return output
'''







            

             
            


        
        