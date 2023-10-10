class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.backwd = [] 
        self.forwd = []

    def visit(self, url: str) -> None:
        self.forwd = []
        self.backwd.append(self.homepage)
        self.homepage = url 

    def back(self, steps: int) -> str:
        while steps and self.backwd:
            self.forwd.append(self.homepage)
            self.homepage = self.backwd.pop()
            steps -= 1
        return self.homepage

    def forward(self, steps: int) -> str:
        while steps and self.forwd:
            self.backwd.append(self.homepage)
            self.homepage = self.forwd.pop()  
            steps -= 1
        return self.homepage


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)