class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for i in range(len(operations)):
            rec = operations[i]
            if rec == '+':
                records.append(records[-1] + records[-2])
            elif rec == 'C':
                records.pop()
            elif rec == 'D':
                records.append(records[-1] * 2)
            else:
                records.append(int(operations[i]))

        return sum(records)