class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,index in enumerate(nums):
             for j,index2 in enumerate(nums):
                if i!=j:
                    if index+index2==target:
                        return [i,j]


        