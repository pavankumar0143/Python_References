'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example,
Given:

s1 = "aabcc",
s2 = "dbbca",
When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, a, b, c):
        m = len(a)
        n = len(b)

        table = [[False for i in range(n+1)] for i in range(m+1)]

        if m+n != len(c):
            return False

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    table[i][j] = True
                elif i == 0 and (b[j-1] == c[j-1]):
                    table[i][j] = table[i][j-1]
                elif j == 0 and a[i-1] == c[i-1]:
                    table[i][j] = table[i-1][j]
                elif a[i-1] == c[i+j-1] and b[j-1] != c[i+j-1]:
                    table[i][j] = table[i-1][j]
                elif a[i-1] != c[i+j-1] and b[j-1] == c[i+j-1]:
                    table[i][j] = table[i][j-1]
                elif a[i-1] == c[i+j-1] and b[j-1] == c[i+j-1]:
                    table[i][j] = table[i-1][j] or table[i][j-1]
        return table[m][n]
