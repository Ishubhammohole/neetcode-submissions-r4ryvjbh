class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for s, d, w in times:
            adj[s].append((d, w))
        
        minHeap = [(0, k)]
        t = 0
        visit = set()
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in adj[n1]:
                heapq.heappush(minHeap, [w1 + w2, n2])
        return t if len(visit) == n else -1

        