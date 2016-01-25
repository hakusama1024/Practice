class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) == 0:
            return res
        s = list(s)
        for i in xrange(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                s[i] = s[i+1] = '-'
                res.append("".join(s))
                s[i] = s[i+1] = '+'
        return res
