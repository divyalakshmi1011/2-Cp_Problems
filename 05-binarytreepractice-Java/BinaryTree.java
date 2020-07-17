
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
		this.root.value = value;
	}

	public boolean search(int value) {
		return search_Node(this.root, value);
	}

	private boolean search_Node(Node r, int val) {
		boolean found = false;
         while ((r != null) && !found)
         {
             int rval = r.value;
             if (val < rval)
                 r = r.left;
             else if (val > rval)
                 r = r.right;
             else
             {
                 found = true;
                 break;
             }
             found = search_Node(r, val);
         }
         return found;
	}
	public static void main(String[] args){
		BinaryTree s = new BinaryTree(1);
		s.root.left = new Node(2);
		s.root.right = new Node(3);
		s.root.left.left = new Node(4);
		s.root.left.right = new Node(5);
		System.out.println(s.search(4));
	}
}