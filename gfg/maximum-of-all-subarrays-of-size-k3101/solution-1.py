import heapq
class Solution:
    def maxOfSubarrays(self, arr, k):
        # sliding window + maxheap
        n = len(arr)
        heap = []
        res = []

        for i in range(n):
            # nya element heap me push
            heapq.heappush(heap, (-arr[i], i))
            # window size bada hua to remove
            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            # agar window complete hai to add
            if i >= k - 1:
                res.append(-heap[0][0])
        return res