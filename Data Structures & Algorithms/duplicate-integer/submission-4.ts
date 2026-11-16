class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const seen = new Set<number>;

        for(const i of nums){
            if(seen.has(i)){
                return true;
            }

            seen.add(i);
        }

        return false;
    }
}
