class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, part = [], []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if self.isPali(s, j, i):
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()

            dfs(j, i + 1)

        dfs(0, 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


# Return is a list of all combinations List[List] -> backtracking is the way to go.
#       Tree looks like:
#               (partition side)            aab       (no partition)
#   split 1 /         |                             \
#    "aa"+"b"      "a"+"ab"                        "aab"
#  "a"+"a"+"b"     "a"+"a"+"b"


#  No, we don't do splits, 
#  In a way, we just need to get all unique full subset combinations of this string
#  After we get the full subsets, we add a subset only if all its constituents are palindromes
#  full subset = subset

# Conditions
# (each letter )
# if palindrome? -> res.append
#

# We don't need to do this for every subset
# the stopping condition is, we need to get a palindrome to start with
# i.e. for aab
# we start by taking "a", a palindrome, great
#    so we consider the other subset of the string recursively
#    i.e. if palindrome("a") and isPalindromic("ab") -> append(["a", "ab"])
# then we take "aa", also a palindrome, great
#    if palindrome("aa") and dfs("b") -> append(["aa","b"])
# then we take "aab", not a palindrome, skip
# and then we are done

# wait, this means the helper function has to return a boolean.


