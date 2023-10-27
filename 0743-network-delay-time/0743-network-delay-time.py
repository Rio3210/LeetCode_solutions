class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_dict = defaultdict(list)
        for u, v, w in times:
            adj_dict[u].append((v, w))

        visited = set()
        min_heap = [(0, k)]
        distance = [float('inf')] * (n + 1)
        distance[k] = 0
        while min_heap:
            curr_dist, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)

            for neighbor, edge_time in adj_dict[curr_node]:
                new_dist = distance[curr_node] + edge_time
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))
        max_time = max(distance[1:])
        return max_time if max_time < float('inf') else -1
        