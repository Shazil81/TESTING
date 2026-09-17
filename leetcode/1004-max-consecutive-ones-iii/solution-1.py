class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # optimal solution two pointer approach tight shrinking
        maxi = 0
        left, right = 0, 0
        zeros = 0
        n = len(nums)
        while right < n:
            # jha pe zero milega wha pe zeros ka count ko badha denge
            if nums[right] == 0:
                zeros += 1
            # zeros ka count agar k se bada ho gya to window invalid
            # window valid krne k liye left ko aage badhayenge
            # or left badhta rhega jab tk zero n mile zero milega tb hi fir zero ka count km hoga
            if zeros > k: # if k jagah while kr denge to better hoga lekin wo tight shrinking nhi hoga
                if nums[left] == 0:
                    zeros -= 1
                left+=1
            # zeros ka count k se km hai yaani window valid hai
            # window valid hai right ko aage badhate jayenge taaki window ka length badhe
            # or maxi ko update krte rhenge
            if zeros <= k:
                maxi = max(maxi, right-left+1)
            right+=1
        return maxi