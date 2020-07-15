// # Write the function pascalsTriangleValue(row, col) 
// # that takes int values row and col, and returns the 
// # value in the given row and column of Pascal's 
// # Triangle where the triangle starts at row 0, and 
// # each row starts at column 0. If either row or col 
// # are not legal values, return None, instead of crashing. 

class pascaltrianglevalue {
	public int fun_pascaltrianglevalue(int row, int col){
		if(row == 0 || col == 0 || row == col) {
			return 1;
		} else {
			return fun_pascaltrianglevalue(row - 1, col - 1) + fun_pascaltrianglevalue(row - 1, col);
		}
	}
}