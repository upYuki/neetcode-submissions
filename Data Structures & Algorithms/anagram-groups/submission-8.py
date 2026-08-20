class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict={}
        for word in strs:
            sorted_word=''.join(sorted(word))
            if sorted_word not in hash_dict:
                hash_dict[sorted_word]=[word]
            else:
                hash_dict[sorted_word].append(word)
        result=list(hash_dict.values())
        return result

                

        