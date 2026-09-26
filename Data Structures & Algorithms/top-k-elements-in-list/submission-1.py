class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = Counter(nums)

        heap = []

        for i, cnt in mp.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, i))
            elif heap[0][0] < cnt:
                heapq.heappop(heap)
                heapq.heappush(heap, (cnt, i))


        res = []

        while heap:
            res.append(heap[0][1])
            heapq.heappop(heap)

        return res
