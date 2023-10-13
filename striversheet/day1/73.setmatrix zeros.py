class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of columns
        # print(m, n)
        for i in range(n):
            for j in range(m):
                if matrix[j][i] == 0:
                    matrix[0][i] = 0
                    matrix[j][0] = 0
        print(matrix)


array = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution().setZeroes(array)
