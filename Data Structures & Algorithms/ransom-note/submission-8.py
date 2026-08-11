class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts={}
        for char in magazine:
            if char in counts:
                counts[char]+=1
            else:
                counts[char]=1

        for char in ransomNote:
            if char not in counts or counts[char]==0:
                return False
            counts[char] -= 1

        return True

        