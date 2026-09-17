class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # sliding window pattern + hashset
        n = len(nums)
        curr_sum = 0
        left = 0
        res = 0
        window_elements = set()
        for right in range(n):
            # agar set me hai to remove kr do left wala index ka element or left badha do
            while nums[right] in window_elements:
                window_elements.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            # set me add kro or curr_sum me
            window_elements.add(nums[right])    
            curr_sum += nums[right]
            # window agar mera k se bada ho jaye tb left wala index se hta do or left badha do
            if right - left + 1 > k:
                window_elements.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            # jab window size == k ho tab res me update kro  
            if right - left + 1 == k:
                res = max(res, curr_sum)
        
        return res