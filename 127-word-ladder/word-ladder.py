from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        while queue:
            word,level=queue.popleft()
            for i in range(len(word)):
                for ch in 'qwertyuioplkjhgfdsazxcvbnm':
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word==endWord:
                        return level+1
                    if new_word in wordset:
                        wordset.remove(new_word)
                        queue.append((new_word,level+1))
        return 0



        