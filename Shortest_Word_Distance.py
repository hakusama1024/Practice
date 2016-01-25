class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        length = len(words)
        res = length+1
        index1 = None
        index2 = None
        for i in xrange(length):
            if words[i] == word1:
                index1 = i
            if words[i] == word2:
                index2 = i
            if index1 != None and index2 != None:
                res = min(res, abs(index1-index2))
        return res
