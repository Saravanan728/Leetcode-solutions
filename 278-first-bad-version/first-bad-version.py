class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            mid = (low + high) // 2

            if isBadVersion(mid):
                high = mid      # mid could be the answer
            else:
                low = mid + 1   # answer must be after mid

        return low
