class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dic={i:[] for i in range(n)}
        
        for e,w in zip(edges,succProb):
            k,j=e
            dic[k].append((w,j))
            dic[j].append((w,k))
        # print(dic)
        visited=set()
        max_heap=[]
        heapq.heappush(max_heap,(-1,start_node))
        
        while max_heap:
            prop,v=heappop(max_heap)
            if v in visited:
                continue
            if v==end_node:
                return -prop
            visited.add(v)
            for w,n in dic[v]:
                if n not in visited:
                    heapq.heappush(max_heap,(prop*w,n))
        return 0
       
