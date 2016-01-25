class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.l = []
        for i in vec2d:
            while len(i):
                self.l.append(i.pop(0))
            

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

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
