class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 : return 0
        if n == 1 : return k
        dp = [0] * n
        dp[0] = k
        dp[1] = k*k
        for i in range(2, n):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])
        return dp[n-1]
