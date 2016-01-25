class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {}
        d['0'] = '0'
        d['6'] = '9'
        d['9'] = '6'
        d['8'] = '8'
        d['1'] = '1'
        l = len(num)
        for i in range(l/2+1):
            if num[i] not in d or num[l-i-1] not in d or d[num[i]] != num[l-i-1]:
                return False
        return True
            
