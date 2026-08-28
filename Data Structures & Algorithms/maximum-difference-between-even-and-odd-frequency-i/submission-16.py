class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)
        mx_odd=0
        mn_even=float('inf')

        for i in freq.values():
            if i%2!=0:
                mx_odd=max(mx_odd,i)
            else:
                mn_even=min(mn_even,i)
        ans=mx_odd-mn_even
        return ans
        