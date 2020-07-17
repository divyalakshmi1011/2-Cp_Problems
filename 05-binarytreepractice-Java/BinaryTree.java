
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
		flag = false;
		searchNode(this.root, value);
		return flag;
	}

	public void searchNode(Node temp, int value){  
        if(root == null){  
          System.out.println("Tree is empty");  
        }  
        else{  
          if(temp.value == value){  
            flag = true;  
               return;  
          }   
          if(flag == false && temp.left != null){  
             searchNode(temp.left, value);  
          }
          if(flag == false && temp.right != null){  
             searchNode(temp.right, value);  
          }  
        }  
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