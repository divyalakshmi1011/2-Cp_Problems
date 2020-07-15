
// isPerfectSquare(n)
// Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
// it is an int that is a perfect square (that is, if there exists an integer m such that
// m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

public class IsPerfectSquare {
	public static boolean isPerfectSquare(int n) {
		if(n < 0) {
			return false;
		} else {
			if(n%2 == 0) {
				return true;
			} else {
				return false;
			}
		}
   }
   public static void main(String[] args) {
      System.out.println(isPerfectSquare(0));
   }
}