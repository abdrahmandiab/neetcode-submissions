class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        q = deque([(beginWord, 1)])
        while q:
            x = q.popleft()
            current_word, steps = x
            if current_word == endWord:
                return steps
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == current_word[i]:
                        continue
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word in word_set:
                        q.append((next_word, steps+1))
                        word_set.remove(next_word)
        return 0

# all given words same length, lowercase english, all distinct
# beginword to endword
#   transform beginWord into any word in wordList on condition they vary by one char
#   may repeat the previous step with new word until it is transformed
#  return minimum number of words within the transformation sequence needed to obtain endWord
#  otherwise 0


#essentially,
# we should map this out into a graph first, where words are connected to
# the other words they are one letter away from
# After that, to sequence path, we just need to find a path between beginWord and endWord.

# Can this be done using DSU?
# can tell if they both are connected, but not really how far they are.







