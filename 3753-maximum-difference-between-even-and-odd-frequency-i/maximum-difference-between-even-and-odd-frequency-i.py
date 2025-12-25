class Solution:
    def maxDifference(self, s: str) -> int:
        odd =0
        even =float('inf')
        d=Counter(s)
        for i in d.values():
            if i%2==1:
                odd = max(odd,i)
            else:
                even = min(even,i)
        return odd - even
        