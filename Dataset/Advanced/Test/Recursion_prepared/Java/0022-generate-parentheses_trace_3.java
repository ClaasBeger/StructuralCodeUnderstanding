package arrays;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {

    Stack<Character> stack = new Stack<>();
    List<String> res = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        backtrack(0, 0, n);
        return res;
    }

    private void backtrack(int openN, int closedN, int n) {
        if (openN == closedN && closedN == n) {
            StringBuilder sb = new StringBuilder();
            for (Character c: stack) {
                sb.append(c);
            }
            res.add(sb.toString());
        }
        if (openN < n) {
            stack.push('(');
            backtrack(openN + 1, closedN, n);
            stack.pop();
        }
        if (closedN < openN) {
            stack.push(')');
            backtrack(openN, closedN + 1, n);
            stack.pop();
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.generateParenthesis(3));
    }
}