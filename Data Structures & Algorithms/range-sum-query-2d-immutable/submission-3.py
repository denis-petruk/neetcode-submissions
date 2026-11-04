class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        length= col2 - col1
        height = row2 - row1
        sum = 0
        position = [row1,col1]
        for i in range(0, height + 1):
            position[1] = col1
            for j in range(0, length + 1):
                sum += self.matrix[position[0]][position[1]]
                position[1] += 1
            position[0] += 1

        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)