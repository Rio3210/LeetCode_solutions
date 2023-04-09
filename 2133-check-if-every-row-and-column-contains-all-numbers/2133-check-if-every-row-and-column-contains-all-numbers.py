class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check=len(matrix[0])
        for row in matrix:
            visited=set()
            for col in row:
                visited.add(col)
            if len(visited)!=check:
                return False
        n=len(matrix)
        for col in range(n):
            visited=set()
            for row in matrix:
                visited.add(row[col])
            if len(visited)!=check:
                return False
        return True