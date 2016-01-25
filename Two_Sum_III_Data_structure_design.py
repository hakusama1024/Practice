class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.d = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.d:
            self.d[number] +=1
        else:
            self.d[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.d:
            if value - num in self.d and (value - num != num or self.d[num] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
