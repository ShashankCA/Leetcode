class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(0, n - 1):
            for j in range(i + 1, n):  
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix

        
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
obj = Solution()
answer = obj.rotate(matrix)

print(answer)



