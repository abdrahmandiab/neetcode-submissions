class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(i1,i2,i3):
            if (i1,i2) in dp:
                return dp[(i1,i2)] 
            if i3 == len(s3):
                return (i1 == len(s1)) and (i2 == len(s2))
            
            result = False
            if i1 < len(s1) and s1[i1] == s3[i3]:
                if dfs(i1+1,i2,i3+1):
                    result = True
            if i2 < len(s2) and s2[i2] == s3[i3]:
                if dfs(i1,i2+1,i3+1):
                    result = True
            dp[(i1,i2)] = result
            return result
        return dfs(0,0,0)






# first thought
# pass a pointer over s3
# for each letter, check if it belongs to s1 or s2 
#                       ^> this needs to check the NEXT in s1 or the NEXT in S2.
# if it belongs to m, m_min++, m_max++, if it belongs to s2, n_min++, n_max++
# if it belongs to both, m_max++ n_max++