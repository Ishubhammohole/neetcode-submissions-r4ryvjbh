class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)
            if second < first:
                new_stone = -1 * (first - second)
                heapq.heappush(stones, new_stone)
        stones.append(0)
        return abs(stones[0])





        