class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const seen = new Map<number, number>;
        const res: number[] = [0, 0];

        for(let i: number = 0; i < nums.length; i++){
            let diff: number = target - nums[i];

            if(seen.has(diff)){
                res[0] = seen.get(diff);
                res[1] = i;
                break;
            }

            seen.set(nums[i], i);
        }

        return res;
    }
}
