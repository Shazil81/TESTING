class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # sliding window + hashmap
        def solve(k):
            freq = {}
            n = len(nums)
            left = 0
            count = 0

            for right in range(n):
                # hashmap me add kiya
                freq[nums[right]] = freq.get(nums[right], 0) + 1
                # jaise hi hashmap ka size bada ho gya k se tb tk remove kiya hashmap se or freq bhi minus kiya
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                
                count += right - left + 1
            
            return count
        # ye is liye ki direct k ka nhi kr skte hai hmko k - (k-1) krna hoga
        return solve(k) - solve(k-1)