class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const stack: string[] = [];
        const pairs = new Map<string, string>();

        pairs.set(')', '(');
        pairs.set(']', '[');
        pairs.set('}', '{');

        for(let i: number = 0; i < s.length; i++){
            if(s[i] == "(" || s[i] == "{" || s[i] == "["){
                stack.push(s[i]);
            } else {
                if(stack.length == 0 || stack.pop() != pairs.get(s[i])){
                    return false;
                }
            }

        }

        return stack.length == 0;
    }
}
