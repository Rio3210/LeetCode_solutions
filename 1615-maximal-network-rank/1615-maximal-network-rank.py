class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for n1,n2 in roads:
            graph[n1].append(n2)
            graph[n2].append(n1)
        # print(graph)
        maxx=float(-inf)
        for i in range(n+1):
            for j in range(i+1,n+1):
                ans=len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    maxx=max(maxx,ans-1)
                else:
                    maxx=max(maxx,ans)
        return maxx