class MapSum:

    def __init__(self):
        self.map=defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.map[key]=val

    def sum(self, prefix: str) -> int:
        ans=0
        for key in self.map.keys():
            if key.startswith(prefix):
                ans+=self.map[key]
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)