class Solution(object):
    def minChanges(self, n, k):
        if (n&k)!=k:
            return -1
        return bin(n^k).count('1')
        