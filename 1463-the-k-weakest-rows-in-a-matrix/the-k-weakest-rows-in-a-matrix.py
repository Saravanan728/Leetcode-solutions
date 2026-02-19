class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = []

        for i, row in enumerate(mat):
            # binary search to find number of soldiers
            low, high = 0, len(row) - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid - 1
            # low = number of soldiers
            strength.append((low, i))

        strength.sort()
        return [idx for _, idx in strength[:k]]
