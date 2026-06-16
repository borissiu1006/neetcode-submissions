class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # slice array < target
        '''
        for i in range(len(numbers) - 1):
            if numbers[i] == target:
                numbers = numbers[:i + 1]
        '''

        i1, i2 = 0, len(numbers) - 1
        while i1 < i2:
            if target - numbers[i2] == numbers[i1]:
                return [i1 + 1, i2 + 1]
            elif target - numbers[i2] > numbers[i1]:
                i1 += 1
            elif target - numbers[i2] < numbers[i1]:
                i2 -= 1