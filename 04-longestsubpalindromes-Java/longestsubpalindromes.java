// # Write the function longestSubpalindrome(s), that takes a string s and returns 
// the longest palindrome that occurs as consecutive characters (not just letters, but 
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!") 
// # returns "b-4-b". If there is a tie, return the lexicographically larger value -- 
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce") 
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions, 
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also, 
// from the explanation above, we see that longestSubpalindrome("aba") is "aba", 
// and longestSubpalindrome("a") is "a".
import java.util.*;

class longestsubpalindromes {
	public static String fun_longestsubpalindromes(String s){
		ArrayList<String> k = substrings(s);
		System.out.println(k);
		ArrayList<String> j = new ArrayList<String>();
		for(int i = 0; i < k.size(); i++) {
			if(palindrome(k.get(i))) {
				j.add(k.get(i));
			}
		}
		System.out.println(j);
		String x = "";
		for(String sr: j){
			if(sr.length() > x.length()){
				x = sr;
			} else if(sr.length() == x.length()) {
				if(sr.compareTo(x) < 0) {
					x = sr;
				}
			}
		}
		return x;
	}
	public static ArrayList<String> substrings(String str) {
		ArrayList<String> l = new ArrayList<String>();
		for (int i = 0; i < str.length(); i++) {
			for (int j = i+1; j <= str.length(); j++) {
				  l.add(str.substring(i,j));
			}
		}
		return l;
	}
	public static boolean palindrome(String s) {
		StringBuffer sbf = new StringBuffer(s);
		sbf.reverse();
		String r = sbf.toString();
		if(r.equals(s)){
			return true;
		} else {
			return false;
		}
	}
	public static void main(String[] args) {
		System.out.println(fun_longestsubpalindromes("abcbaABCBA"));
	}
}
