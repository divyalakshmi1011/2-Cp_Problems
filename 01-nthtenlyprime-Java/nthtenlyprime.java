// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


class nthtenlyprime {
	public static boolean isprime(int n) {
		int count = 0;
		for(int i = 1; i <= n; i++) {
			if(n % i == 0) {
				count += 1;
			}
		}
		if(count == 2) {
			return true;
		} else {
			return false;
		}
	}
	public static int fun_nthtenlyprime(int n){
		if( n == 0) {
			return 19;
		}
		// String a = Integer.toString(n);
		int c = 0;
		int t = 20;
		while(c <= n) {
		String a = Integer.toString(t);
		if(a.length() == 1) {
			t += 1;
		} else {
			if(isprime(t)) {
				// System.out.println("t" + t);
			int sum = 0;
			for(int i = 0; i < a.length(); i++) {
				int b = Character.getNumericValue(a.charAt(i));
				sum += b;
			}
			if(sum == 10) {
				c += 1;
				if(c == n) {
					break;
				} else {
					t += 1;
				}
			} else {
				t += 1;
			}
		} else {
			t += 1;
		}
	}
	}
	return t;
	}
	public static void main(String[] args) {
		System.out.println(isprime(50));
		System.out.println(fun_nthtenlyprime(0));
		System.out.println(fun_nthtenlyprime(15));
		System.out.println(fun_nthtenlyprime(20));
		System.out.println(fun_nthtenlyprime(25));
		System.out.println(fun_nthtenlyprime(10));
	}
}