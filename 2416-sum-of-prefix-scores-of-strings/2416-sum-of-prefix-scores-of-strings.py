class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def get_prefix_count(self, word):
        node = self.root
        count = 0
        for char in word:
            node = node.children[char]
            count += node.count
        return count


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        prefix_scores = []
        for word in words:
            prefix_count = trie.get_prefix_count(word)
            prefix_scores.append(prefix_count)

        return prefix_scores