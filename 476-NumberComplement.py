class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = bin(num)[2::]
        d = ''
        for c in s:
            if c == '1':
                d += '0'
            else :
                d += '1'
        return int(d, 2)
