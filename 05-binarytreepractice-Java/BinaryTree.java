
class Node {
	public int value;
	public Node left, right;
	public Node(int value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

public class BinaryTree {
	public Node root;
	public static boolean flag = false;  

	public BinaryTree(int value) {
		this.root = new Node(value);
	}

	public boolean search(int value) {
		return search_Node(this.root, value);
	}

	private boolean search_Node(Node temp, int value) {
		if(root == null){  
		     flag = false;
		  }  
		  else{  
			//If value is found in the given binary tree then, set the flag to true  
			if(temp.value == value){  
			  flag = true;   
			}  
			//Search in left subtree  
			if(flag == false && temp.left != null){  
			   search_Node(temp.left, value);  
			}  
			//Search in right subtree  
			if(flag == false && temp.right != null){  
			   search_Node(temp.right, value);  
			}  

		  }
		  return flag;  
	}
	public static void main(String[] args){
		BinaryTree s = new BinaryTree(1);
		s.root.left = new Node(2);
		s.root.right = new Node(3);
		s.root.left.left = new Node(4);
		s.root.left.right = new Node(5);
		System.out.println(s.search(2));
	}
}