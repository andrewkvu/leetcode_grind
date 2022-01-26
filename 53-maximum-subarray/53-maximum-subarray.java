class Solution {
    public int maxSubArray(int[] nums) {
        int runningSum = 0;
        int max = nums[0];
        
        for (int i = 0; i < nums.length; i++) {
            if (runningSum < 0)
                runningSum = 0;
            runningSum += nums[i];
            max = Math.max(max, runningSum);
        }
        return max;
    }
}