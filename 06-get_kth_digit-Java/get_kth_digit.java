// # Write the function pascalsTriangleValue(row, col) 
// # that takes int values row and col, and returns the 
// # value in the given row and column of Pascal's 
// # Triangle where the triangle starts at row 0, and 
// # each row starts at column 0. If either row or col 
// # are not legal values, return None, instead of crashing. 

class get_kth_digit {
	public int fun_get_kth_digit(int digit, int k){
		// your code goes here
		String s = digit + "";
		if(k < s.length()) {
			StringBuilder input1 = new StringBuilder(); 
  
			// append a string into StringBuilder input1 
			input1.append(s); 
	
			// reverse StringBuilder input1 
			input1 = input1.reverse();
			return Integer.parseInt((input1.toString().charAt(k)) + "");
    
		}
		return 0;
	}
}