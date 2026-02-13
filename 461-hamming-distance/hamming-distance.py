class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        h=x^y
        count=0
        while h:
            h=h&(h-1)
            count+=1
        return count
        