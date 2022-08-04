class Solution:
    def rotate(matrix: list[list[int]]) -> None:
        for i in range(len(matrix)-1):
            for j in range(i+1, len(matrix)):
                s = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = s
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
    print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
