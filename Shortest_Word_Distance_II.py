class WordDistance(object):
    def __init__(self, words):
        from collections import defaultdict
        self.d = defaultdict(list)
        self.n = len(words)
        for i in xrange(len(words)):
            self.d[words[i]].append(i)
    
    def shortest(self, word1, word2):
        a = self.d[word1]
        b = self.d[word2]
        ans = self.n
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                ans = min(ans, b[j] - a[i])
                i += 1
            else:
                ans = min(ans, a[i] - b[j])
                j += 1
        return ans


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
