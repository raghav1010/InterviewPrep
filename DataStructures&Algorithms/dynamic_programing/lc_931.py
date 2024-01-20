class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                if (j == 0):
                    A[i][j] = A[i][j] + min(A[i - 1][j], A[i - 1][j + 1])
                if (j == len(A[i]) - 1):
                    A[i][j] = A[i][j] + min(A[i - 1][j], A[i - 1][j - 1])
                if (j > 0 and j < len(A[i]) - 1):
                    A[i][j] = A[i][j] + min(A[i - 1][j], A[i - 1][j - 1], A[i - 1][j + 1])
        print(A)
        return min(A[-1])
