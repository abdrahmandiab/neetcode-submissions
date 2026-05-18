class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s=">OXUZODYXAZV", t = "XYZ"
        if t == "":
            return ""
        window, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        res, resLen = [-1,-1] , float("infinity")
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in countT:
                window[c] = window.get(c, 0) + 1
                if window[c] == countT[c]:
                    have +=1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)

                c = s[l]
                if c in countT:
                    window[c] = window.get(c,0) - 1
                    if window[c] < countT[c]:
                        have-=1
                l+=1
        
        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""