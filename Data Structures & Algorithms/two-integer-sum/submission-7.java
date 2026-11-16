class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap();
        int[] result = {0, 0};

        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];

            if(seen.containsKey(diff)){
                result[0] = seen.get(diff);
                result[1] = i;
                break;
            }

            seen.put(nums[i], i);
        }

        return result;
    }
}
