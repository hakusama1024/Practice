class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        flag = False
        for i in dic:
            if dic[i]%2 != 0:
                if flag == False:
                    flag = True
                else:
                    return False
        return True
