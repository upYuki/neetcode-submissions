class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        single_digits=int("".join(str(x) for x in digits))
        num = single_digits+1
        hashlist=[]

        return [int(i) for i in str(num)]


        