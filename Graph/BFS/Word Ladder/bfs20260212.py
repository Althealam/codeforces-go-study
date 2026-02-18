from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        lower_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        def bfs():
            queue = deque()
            queue.append((beginWord, 0))

            visited = set()
            visited.add(beginWord)

            while queue:
                current_word, step = queue.popleft()
                if current_word==endWord:
                    return step
                
                for i in range(len(current_word)):
                    for letter in lower_letters:
                        new_word = current_word[:i]+letter+current_word[i+1:]

                        if new_word in word_set and new_word not in visited:
                            visited.add(new_word)
                            queue.append((new_word, step+1))
            return -1
        return bfs()+1

sol = Solution()
beginWord ="hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
res = sol.ladderLength(beginWord, endWord, wordList)
print(res)