class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cells = len(matrix), len(matrix[0])

        # create a map, with +1 size on both xy
        # for each cell, store culumlative total instead of their value (-right)
        self.matrix_sum = [[0]* (cells + 1) for i in range(rows + 1)]

        for row in range(rows):
            prefix = 0
            for cell in range(cells):
                prefix += matrix[row][cell]
                above = self.matrix_sum[row][cell + 1] # since matrix is +1 on both xy
                self.matrix_sum[row + 1][cell + 1] = prefix + above 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1 # as above

        sum_ul = self.matrix_sum[row1-1][col1-1]
        sum_lr = self.matrix_sum[row2][col2]

        above = self.matrix_sum[row1 - 1][col2]
        left = self.matrix_sum[row2][col1 - 1]

        return sum_lr - above - left + sum_ul


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)