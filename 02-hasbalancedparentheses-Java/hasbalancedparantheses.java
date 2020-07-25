// # Write the function hasBalancedParentheses, which takes a string and returns True 
// # if that code has balanced parentheses and False otherwise (ignoring all 
// # 	non-parentheses in the string). We say that parentheses are balanced if each 
// # right parenthesis closes (matches) an open (unmatched) left parenthesis, 
// # and no left parentheses are left unclosed (unmatched) at the end of the text. 
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) (" 
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as 
// # you iterate over the string.
import java.util.*;
 
class hasbalancedparantheses {
	public static boolean fun_hasbalancedparantheses(String s){
		ArrayList<Character> l = new ArrayList<Character>();
		for(int i = 0; i < s.length(); i++){
			if(s.charAt(i) == '(') {
				l.add(s.charAt(i));
			} else {
				if(l.size() == 0) {
					return false;
				}
				Character curchar = l.get(l.size() - 1);
				if(curchar == '(') {
					if(s.charAt(i) != ')') {
						return false;
					}
				}
			}
		}
		if(l.size() > 0) {
			return false;
		}
		return true;
	}
	public static void main(String[] args) {
		System.out.println(fun_hasbalancedparantheses("( ( ( ( )3)))  "));
	}
}
	