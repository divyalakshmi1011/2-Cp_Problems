
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
	public BinaryTree(int value) {
		this.root = new Node(value);
	}
    public boolean search(int value) {
		Node x = this.root;
		return searchNode(x, value);
	}
	public boolean searchNode(Node node,int value) {
		if (node == null)  
          return false;  
		if (node.value == value)  
			return true;  
		boolean res1 = searchNode(node.left, value);  
		if(res1) return true;
		boolean res2 = searchNode(node.right, value);  
		return res2;
		}

	
	public static void main(String[] args){
		BinaryTree s = new BinaryTree(1);
		s.root.left = new Node(2);
		s.root.right = new Node(3);
		s.root.left.left = new Node(4);
		s.root.left.right = new Node(5);
		// s.searchNode(s.root,6);
		// System.out.println(flag);
		System.out.println(s.search(4));
		System.out.println(s.search(6));
	}
}