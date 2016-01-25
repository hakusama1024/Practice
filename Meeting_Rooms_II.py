# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        size = len(intervals)
        if size == 0 : return 0
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        minRoom = 0; curRoom = 0
        s=0; e=0
        while s < size:
            if start[s] < end[e]:
                curRoom+=1
                s+=1
                minRoom = max(minRoom, curRoom)
            else:
                curRoom-=1
                e+=1
        return minRoom
        
        
        
        
