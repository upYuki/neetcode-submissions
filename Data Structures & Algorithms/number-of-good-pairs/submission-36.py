class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}  # Keeps track of how many times we've seen each number
        pairs = 0
        
        for num in nums:
             if num in counts:
            # If we've seen this number 2 times before, it creates 2 new pairs!
                 pairs += counts[num]
                 counts[num] += 1
             else:
                 counts[num] = 1
            
        return pairs