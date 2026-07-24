import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap_list = [(-value, key) for key, value in counts.items()]
        heapq.heapify(heap_list)
        res = []
        for i in range(k):
            neg_value, key = heapq.heappop(heap_list)
            res.append(key)
        return res