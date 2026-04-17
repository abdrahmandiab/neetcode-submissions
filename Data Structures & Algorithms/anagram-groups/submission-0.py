class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_to_output_idx = {}
        output = []
        for string in strs:
            dicto = {}
            for char in string: #populate dict
                dicto[char] = dicto.get(char,0) + 1
            key = tuple(sorted(dicto.items()))
            output_idx = dict_to_output_idx.get(key,None)
            if output_idx is not None:
                output[output_idx].append(string)
            else:
                dict_to_output_idx[key] = len(output)
                output.append([string])
    
        return output
