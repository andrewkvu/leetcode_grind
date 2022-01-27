class Solution {
    public int singleNumber(int[] nums) {
        List<Integer> set = new ArrayList<Integer>();
        for (int i = 0 ; i < nums.length; i++) {
            if (!set.contains(nums[i]))
                set.add(nums[i]);
            else
                set.remove(new Integer(nums[i]));
        }
        return set.get(0);
    }
}