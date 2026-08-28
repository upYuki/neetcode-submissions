class Solution:
    def maxDifference(self, s: str) -> int:
        hashdict={}
        even=set()
        odd=set()
        for i in s:
            if i not in hashdict:
                hashdict[i]=1
            else:
                hashdict[i]+=1
        top2=sorted(hashdict.values(),reverse=True)[:2]
        for i in hashdict.values():
            if i%2==0:
                even.add(i)
            else:
                odd.add(i)
        max_odd=max(odd)
        min_even=min(even)
        
        ans=max_odd-min_even
        return ans
        