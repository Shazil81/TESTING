class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Sliding window
        if k <= 1: # base case
            return 0
            
        left = 0
        curr_prod = 1
        count = 0
        n = len(nums)
        for right in range(n):
            curr_prod *= nums[right]
            
            while curr_prod >= k and left <= right:
                curr_prod //= nums[left]
                left += 1
            # ki jitne elements pehle aaye wo bhi to subarray me count hoga  
            count += (right - left + 1)
        
        return count