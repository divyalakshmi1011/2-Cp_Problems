/**Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions.**/

class recursion {
	public static int get_fib(int n){
		if(n <= 1) {
			return n;
		}
		return get_fib(n - 1) + get_fib(n - 2);
	}
	public static void main(String[] args) {
		System.out.println(get_fib(9));
	}
}