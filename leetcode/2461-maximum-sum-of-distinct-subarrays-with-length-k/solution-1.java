class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        long maxSum = 0;
        long currentSum = 0;
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            // Window me naya element add karo
            currentSum += nums[i];
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);

            // Jab window size k se bada ho jaye, to purana element hatao
            if (i >= k) {
                int outNum = nums[i - k];
                currentSum -= outNum;
                if (map.get(outNum) == 1) {
                    map.remove(outNum);
                } else {
                    map.put(outNum, map.get(outNum) - 1);
                }
            }

            // Jab window size exactly k ho aur saare elements distinct ho
            if (i >= k - 1 && map.size() == k) {
                maxSum = Math.max(maxSum, currentSum);
            }
        }

        return maxSum;
    }
}