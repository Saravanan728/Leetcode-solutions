class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        if len(s) != len(indices):
            return ""
        char=dict(zip(indices,s))
        ans="".join(v for k,v in sorted(char.items()))
        return ans
