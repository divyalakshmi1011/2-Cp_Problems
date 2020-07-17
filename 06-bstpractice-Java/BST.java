
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
    }

    private void insert(Node node, int value) {
    	// Your code goes here
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

}