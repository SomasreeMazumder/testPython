mod = 1e9 + 7
dp = [[[[-1] * 4 for i in range(101)] for j in range(101)] for k in range(101)];


class Solution:
    def solve(self, p, q, r, last):
        if (p < 0 or q < 0 or r < 0):
            return 0

        if (p == 1 and q == 0 and r == 0 and last == 0):
            return 1

        if (p == 0 and q == 1 and r == 0 and last == 1):
            return 1
        if (p == 0 and q == 0 and r == 1 and last == 2):
            return 1

        if (dp[p][q][r][last] != -1):
            return dp[p][q][r][last]

        if (last == 0):
            dp[p][q][r][last] = (self.solve(p - 1, q, r, 1) + self.solve(p - 1, q, r, 2)) % mod

        elif (last == 1):
            dp[p][q][r][last] = (self.solve(p, q - 1, r, 0) + self.solve(p, q - 1, r, 2)) % mod

        else:
            dp[p][q][r][last] = (self.solve(p, q, r - 1, 0) + self.solve(p, q, r - 1, 1)) % mod

        return dp[p][q][r][last]

    def CountWays(self, p, q, r):
        # Code here
        return int(((self.solve(p, q, r, 0) + self.solve(p, q, r, 1) + self.solve(p, q, r, 2))) % mod)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        p, q, r = input().split()
        p = int(p);
        q = int(q);
        r = int(r);
        ob = Solution()
        ans = ob.CountWays(p, q, r)
        print(ans)
# } Driver Code Ends