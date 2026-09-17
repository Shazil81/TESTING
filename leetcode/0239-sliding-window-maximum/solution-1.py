import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window + maxheap
        n = len(nums)
        heap = []
        res = []

        for i in range(n):
            # nya element heap me push
            heapq.heappush(heap, (-nums[i], i))
            # window size bada hua to remove
            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            # agar window complete hai to add
            if i >= k - 1:
                res.append(-heap[0][0])
        return res

        # TC : O(nlogn)
        # SC : O(n)
