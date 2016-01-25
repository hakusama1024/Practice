class ZigzagIterator(object):
    

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.l = []
        while len(v1) and len(v2):
            self.l.append(v1.pop(0))
            self.l.append(v2.pop(0))
        while len(v1):
            self.l.append(v1.pop(0))
        while len(v2):
            self.l.append(v2.pop(0))
        

    def next(self):
        """
        :rtype: int
        """
        return self.l.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.l) != 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
