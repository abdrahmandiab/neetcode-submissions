class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}
        for char in s:
            dict_1[char] = dict_1.get(char,0) +1
        for char in t:
            dict_2[char] = dict_2.get(char,0) +1
        
        if dict_1 == dict_2:
            return True
        else:
            return False