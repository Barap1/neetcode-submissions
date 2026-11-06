
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_i = {}
        for i in s:
            if i in dict_i:
                dict_i[i] += 1
            else:
                dict_i[i] = 1
        
        dict_j = {}
        for i in t:
            if i in dict_j:
                dict_j[i] += 1
            else:
                dict_j[i] = 1

        return dict_i == dict_j
        

    