class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)

        for s in strings:
            shift = [str((ord(c) - ord(s[0]))%26) for c in s]
            stringkey = ','.join(shift)
            d[stringkey].append(s)
            
        return map(sorted, d.values())
