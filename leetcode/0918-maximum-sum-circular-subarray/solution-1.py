class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # kadane'n algo (logic yhi hai ki total sum se min sum ko minus kr do tb hi wo circular wala max dega)
        total_sum = 0
        max_sub = nums[0]
        min_sub = nums[0]
        curr_max = 0
        curr_min = 0

        for num in nums:
            total_sum += num
            curr_max = max(num, curr_max+num)
            max_sub = max(max_sub, curr_max)

            curr_min = min(num, curr_min+num)
            min_sub = min(min_sub, curr_min)

        if max_sub < 0:
            return max_sub

        circular_max = total_sum - min_sub

        return max(max_sub, circular_max)