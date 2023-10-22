class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
    def search(self, word: str) -> bool:
        curr = self.root
        prefix=""
        for ch in word:
            if ch not in curr.children:
                break
            curr = curr.children[ch]
            prefix+=ch
            if curr.is_end:
                return prefix
        return word
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root=Trie()
        for word in dictionary:
            root.insert(word)
        res=""
        for s in sentence.split():
            if res:
                res=res+ " " 
            res+=root.search(s)
        return res
        
        # st=sentence.split()
        # d=set(dictionary)
        # ans=[]
        # for w in st:
        #     flag=False
        #     for i in range(len(w)):
        #         sub=w[:i+1]
        #         if sub in d:
        #             ans.append(sub)
        #             flag=True
        #             break
        #     if flag==False:
        #         ans.append(w)
        # # print(ans)
        # return " ".join(ans)