class Solution: #wasitacaroracatisaw
    def isPalindrome(self, s: str) -> bool:
        translation_table = dict.fromkeys(map(ord," !@#$\'\\?,:;."), None)
        s = s.translate(translation_table).lower()
        print(s)
        n = len(s)
        return s[0:int(n/2)] == s[::-1][0:int(n/2)]
        # counter = 0
        # for char in s[::-1]:
        #     if char == " ":
        #         #skip
        #         continue
        #     else:
        #         if s[counter] == " ":
        #             counter+=1
        #             continue
        #         else:
        #             if s[]