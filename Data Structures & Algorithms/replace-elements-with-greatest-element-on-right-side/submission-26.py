class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi=-1
        for i in range(len(arr)-1,-1,-1):
            new_max=max(maxi,arr[i])
            arr[i]=maxi
            maxi=new_max
        return arr


            
        
        