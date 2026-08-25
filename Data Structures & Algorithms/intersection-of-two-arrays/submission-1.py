class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset=set()
        for i in nums1:
            if i in nums2:
                hashset.add(i)
        hashlist=list(hashset)
        return hashlist

        