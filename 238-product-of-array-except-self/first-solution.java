class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        
        left[0] = 1;
        right[nums.length - 1] = 1;
        
        for (int i = 1; i < nums.length; i++) {
            left[i] = nums[i - 1] * left[i - 1];
        }
        /*
            left[0] = 1;
            
            left[1] = nums[0] * left[0] = 1 * 1 = 1;
            left[2] = nums[1] * left[1] = 2 * 1 = 2;
            left[3] = nums[2] * left[2] = 3 * 2 = 6;
            
        */
        
        for (int i = nums.length - 2; i >= 0; i--) {
            right[i] = nums[i + 1] * right[i + 1];
        }
        
        /*
            right[3] = 1;
            
            right[2] = 4 * 1 = 4;
            right[1] = 3 * 4 = 12;
            right[0] = 2 * 12 = 24;
        */
        
        for (int i = 0; i < left.length; i++) {
            answer[i] = left[i] * right[i];
        }
        
        return answer;
    }
}
