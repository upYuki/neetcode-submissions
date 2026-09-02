class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,r=0,x
        res=0
        while l<=r:
            n = l + ((r-l)//2)
            m=n*n
            if m>x:
                r=n-1
            elif m<x:
                res=n
                l=n+1
            else:
                return n
        return res
