class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window based hai 
        n = len(nums)
        left = 0
        curr_sum = 0
        mini_length = float('inf')
        
        for right in range(n):
            curr_sum += nums[right]
            # jaise hi mera condition fall krega hm length count kr lenge or min me update 
            while curr_sum >= target:
                mini_length = min(mini_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        if mini_length != float('inf'):
            return mini_length
        return 0