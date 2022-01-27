class Solution {
    public int singleNumber(int[] nums) {
        // weird bit manipulation
        int result = 0;
        
        for (int i = 0; i < nums.length; i++) {
            result ^= nums[i];
        }
        
        return result;
        
        /*
             1 ^ 9 = 8
             8 ^ 1 = 9
             8 ^ 9 = 1
             0 ^ 2 = 2
             2 ^ 2 = 0
             
        */
    }
}