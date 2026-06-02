class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            elif i in d:
                d[i] += 1
        
        order = []
        for num, counts in d.items():
            order.append([counts, num])

        order.sort(reverse=True)

        requirement = order[:k]
        output = []

        for [counts, num] in requirement:
            output.append(num)

        return output

       



        
        



        