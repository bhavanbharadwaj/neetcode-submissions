import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dictionary = {}

        def helper(s):
            dictionary = {}
            for char in string.ascii_lowercase:
                dictionary[char] = 0
            
            for char in s:
                dictionary[char] += 1
            
            if str(dictionary) not in result_dictionary:
                result_dictionary[str(dictionary)] = [s]
            else:
                result_dictionary[str(dictionary)].append(s)
            
        
        for word in strs:
            helper(word)
        
        return [value for key, value in result_dictionary.items()]