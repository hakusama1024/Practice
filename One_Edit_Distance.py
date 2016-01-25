class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n, m = len(s), len(t)
        if abs(n - m) > 1:
            return False
        k = min(n, m)
        i = j = 0
        while i < k and s[i] == t[i]:
            i += 1
        while j < k - i and s[-j-1] == t[-j-1]:
            j += 1
        return max(n, m) - (i + j) == 1
