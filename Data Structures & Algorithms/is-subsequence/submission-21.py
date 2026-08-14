class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        s_index=0
        for char in t:
            if char==s[s_index]:
                s_index+=1
            if len(s)==s_index:
                return True
        return False



        