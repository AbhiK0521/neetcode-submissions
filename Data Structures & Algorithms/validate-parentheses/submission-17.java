class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> pairs = new HashMap<>();

        pairs.put(')', '(');
        pairs.put(']', '[');
        pairs.put('}', '{');
        
        for(char i : s.toCharArray()){
            if(pairs.containsKey(i)){
                if(stack.isEmpty() || stack.peek() != pairs.get(i)){
                    return false;
                } else{
                    stack.pop();
                }
                
            } else {
                stack.push(i);
                
            }
        }

        return stack.isEmpty();
    }
}
