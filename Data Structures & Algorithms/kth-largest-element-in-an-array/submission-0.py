class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for i in nums:
            maxHeap.append(-i)
        heapq.heapify(maxHeap)
        res = 0
        while k > 0:
            res = heapq.heappop(maxHeap)
            k -= 1
        return -res

        