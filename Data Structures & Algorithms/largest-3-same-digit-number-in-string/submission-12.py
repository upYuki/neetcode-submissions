class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result=""
        for i in range(len(num)-2):
            number=num[i:i+3]

            if number[0]*3==number:
                result=max(result,number)
        return result
        