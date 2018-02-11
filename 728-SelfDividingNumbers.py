class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l = []
        for i in range(left, (right+1)):
            result = 0
            for x in str(i):
                if x == '0':
                    result = 100
                else:
                    result += i%int(x)
            if result == 0:
                l.append(i)
        return l
