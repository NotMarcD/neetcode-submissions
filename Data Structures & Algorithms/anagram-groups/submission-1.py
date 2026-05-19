class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for string in strs:
            str_value = self.getHash(string);
            if str_value not in dct:
                dct[str_value] = [string]
            else:
                lst = dct[str_value]
                lst.append(string)
        soln = []
        for string_lst in dct.values():
            soln.append(string_lst)
        return soln
    
    def getHash(self, string: str):
        alpha_lst = [0] * 26
        freq = []
        for c in string:
            alpha_lst[ord(c) - ord('a')] += 1

        print(alpha_lst)
        for i in range(26):
            freq.append(str(alpha_lst[i]))
            freq.append("|")
        print(''.join(freq))
        return ''.join(freq)
        
