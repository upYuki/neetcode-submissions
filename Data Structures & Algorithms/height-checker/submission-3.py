class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        expected=sorted(heights)
        if expected==heights:
            return 0
        for i in range(len(expected)):
            if expected[i]!=heights[i]:
                count+=1
        return count

        