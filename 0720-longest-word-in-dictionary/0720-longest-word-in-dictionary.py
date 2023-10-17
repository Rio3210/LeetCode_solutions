class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.string = None


class Trie:

    def __init__(self):
        self.root = TrieNode()
        
        
    def charToIndex(self,char):
        return ord(char) - ord("a")

    def insert(self, word: str) -> None:

        tempRoot = self.root

        for char in word:

            indx = self.charToIndex(char)

            if not tempRoot.children[indx]:
                tempRoot.children[indx] = TrieNode()

            tempRoot = tempRoot.children[indx]


        tempRoot.string = word


class Solution:

    def __init__(self):
        self.ans = ""
        

    def dfs(self, root):
        for child in root.children:
            if child and child.string:
                if len(child.string) > len(self.ans):
                    self.ans = child.string

                self.dfs(child)
    
    
    def longestWord(self, words: List[str]) -> str:

        trie = Trie()
       
        for word in words:
            trie.insert(word)

        
        self.dfs(trie.root)
        
        return self.ans

        


        