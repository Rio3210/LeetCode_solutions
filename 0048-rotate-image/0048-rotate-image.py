class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        """
        Do not return anything, modify matrix in-place instead.
        """
        