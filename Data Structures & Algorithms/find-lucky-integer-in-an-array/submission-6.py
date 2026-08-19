class Solution:
    def findLucky(self, arr: List[int]) -> int:
        occurences={}
        count=0
        for i in arr:
            if i in occurences:
                occurences[i]+=1
            else:
                occurences[i]=1
        sorted_occurences=dict(sorted(occurences.items()))
        for i in sorted_occurences:
            if i==sorted_occurences[i] and i>i-1:
                count=i
        if count==0:
            count=-1
        return count


        