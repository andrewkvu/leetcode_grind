class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        
        answer[0] = 1;
        
        for (int i = 1; i < nums.length; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }
        /*
            answer[0] = 1;
            
            answer[1] = nums[0] * answer[0] = 1 * 1 = 1;
            answer[2] = nums[1] * answer[1] = 2 * 1 = 2;
            answer[3] = nums[2] * answer[2] = 3 * 2 = 6;
            
        */
        
        int right = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            answer[i] = answer[i] * right;
            right = right * nums[i];
        }
        
        return answer;
    }
}