
class Node {
    public int value;
    public Node left, right;
    public Node(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

public class BST {
    public Node root;
    public static boolean flag = false; 
    public BST(int value) {
        this.root = new Node(value);
    }

    public void insert(int value) {
      // Your code goes here
      // System.out.println("divya");
      Node x = this.root;
      this.root = insert(x,value);
    }

    private Node insert(Node node, int value) {
      // System.out.println("divya");
      if (node == null) return new Node(value);
    	if(value < node.value) {
        node.left = insert(node.left,value);
      } else if(value > node.value) {
        node.right = insert(node.right,value);
      } else {
        node.value = value;
      }
      return node;
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
      public static void main(String[] args) {
        BST s = new BST(4);
        System.out.println(s.search(1));
        s.insert(2);
        s.insert(1);
        s.insert(3);
        s.insert(5);
        System.out.println(s.search(1));
      }  

}