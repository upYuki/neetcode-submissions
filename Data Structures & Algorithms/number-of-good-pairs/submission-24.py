class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashset=set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]==nums[j]:
                    pair=(i,j)
                    opp_pair=(j,i)
                    if opp_pair not in hashset:
                        hashset.add(pair)
        count=len(hashset)
        return count
        