class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       hashmap = Counter(nums)
       heap = [(-freq, num) for num, freq in hashmap.items()]
       heapq.heapify(heap)

       top_k_el = []
       for _ in range(k):
        top_k_el.append(heapq.heappop(heap)[1])
       return top_k_el
        


        