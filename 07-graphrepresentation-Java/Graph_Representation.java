import java.util.*;
import java.util.stream.Collectors;

class Node{
	int value;
	ArrayList<Edge> edges;
	Node(int value){
		this.value = value;
		edges = new ArrayList<Edge>();
	}
} 

class Edge{
	int value;
	Node node_from;
	Node node_to;
	Edge(int value,Node node_from, Node node_to){
		this.value = value;
		this.node_from = node_from;
		this.node_to = node_to;
	}
}

public class Graph_Representation{
	ArrayList<Node> nodes;
	ArrayList<Edge> edges;
	Graph_Representation(){
		this.nodes = new ArrayList<Node>();
		this.edges = new ArrayList<Edge>();
	}

	public void insert_node(int value){
		Node new_node = new Node(value);
		this.nodes.add(new_node);
	}

	public void insert_edge(int val, int node_from_val, int node_to_val){
		Node from_found = null;
		Node to_found = null;
		for(int i = 0; i < this.nodes.size(); i++){
			if(node_from_val == nodes.get(i).value){
				from_found = nodes.get(i);
			}
			if(node_to_val == nodes.get(i).value){
				to_found = nodes.get(i);
			}
		}
		if(from_found == null){
			from_found = new Node(node_from_val);
			this.nodes.add(from_found);
		}
		if(to_found == null){
			to_found = new Node(node_to_val);
			this.nodes.add(to_found);
		}
		Edge new_edge = new Edge(val, from_found, to_found);
		from_found.edges.add(new_edge);
		to_found.edges.add(new_edge);
		this.edges.add(new_edge);

	}

	public ArrayList<ArrayList<Integer>> get_edge_list(){
		// """Don't return a list of edge objects!
        // Return a list of list that looks like this:
        // [Edge Value, From Node Value, To Node Value]"""
		ArrayList<ArrayList<Integer>> r = new ArrayList<ArrayList<Integer>>();
		for(int i = 0; i < edges.size();i++){
			ArrayList<Integer> x = new ArrayList<Integer>();
			x.add(edges.get(i).value);
			x.add(edges.get(i).node_from.value);
			x.add(edges.get(i).node_to.value);
			r.add(x);
		}
        return r;
	}

	public ArrayList<ArrayList<Integer>> get_adjacency_list(){
		// """Don't return any Node or Edge objects!
        // You'll return a list of lists.
        // The indecies of the outer list represent
        // "from" nodes.
        // Each section in the list will store a list of To Node
		ArrayList<ArrayList<Integer>> r = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> n = new ArrayList<Integer>();
		for(int h = 0; h < nodes.size();h++){
			n.add(nodes.get(h).value);
		}
		int a = Collections.max(n);
		for(int j = 0; j < a + 1; j++){
			ArrayList<Integer> x = new ArrayList<Integer>();
		for(int i = 0; i < edges.size();i++){
			// System.out.println(edges.get(i).node_from.value + " " + j );
			if(edges.get(i).node_from.value == j){
				// System.out.println("divya");
				x.add(edges.get(i).node_to.value);
				// System.out.println(x);
			}
			}
			// System.out.println("after" + x);
			r.add(x);
			// System.out.println("after" + r);
			// x.clear();
			// System.out.println("clear" + x);
		}
			return r;
		}

	public ArrayList<ArrayList<Integer>> get_adjacency_matrix(){
		// """Return a matrix, or 2D list.
        // Row numbers represent from nodes,
        // column numbers represent to nodes.
        // Store the edge values in each spot,
		// and a 0 if no edge exists."""
		ArrayList<Integer> n = new ArrayList<Integer>();
		for(int h = 0; h < nodes.size();h++){
			n.add(nodes.get(h).value);
		}
		int a = Collections.max(n);
		int[][] matrix = new int[a][a];
		Arrays.fill(matrix, 0);
		for(int i = 0; i < edges.size();i++){
			matrix[edges.get(i).node_from.value][edges.get(i).node_to.value] = edges.get(i).value;
		}
		ArrayList<ArrayList<Integer>> r = new ArrayList<ArrayList<Integer>>();
		for (int[] array : matrix) {
			//This will add int[] object into the list, and not the int values.
			ArrayList<Integer> p = new ArrayList<Integer>();
			for (int i = 0; i < array.length;i++){
				p.add(array[i]);
			}
			r.add(p);
		}
		return r;
	}

	public static void main(String[] args){
		Graph_Representation graph = new Graph_Representation();
		graph.insert_edge(100, 1, 2);
		graph.insert_edge(101, 1, 3);
		graph.insert_edge(102, 1, 4);
		graph.insert_edge(103, 3, 4);
		ArrayList<ArrayList<Integer>> r= graph.get_adjacency_matrix();
		ArrayList<ArrayList<Integer>> a = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> a1 = new ArrayList<Integer>();
		a1.add(0);a1.add(0);a1.add(0);a1.add(0);a1.add(0);a.add(a1);
		a1 = new ArrayList<Integer>();a1.add(0);a1.add(0);a1.add(100);a1.add(101);a1.add(102);a.add(a1);
		a1 = new ArrayList<Integer>();a1.add(0);a1.add(0);a1.add(0);a1.add(0);a1.add(0);a.add(a1);
		a1 = new ArrayList<Integer>();a1.add(0);a1.add(0);a1.add(0);a1.add(0);a1.add(103);a.add(a1);
		a1 = new ArrayList<Integer>();a1.add(0);a1.add(0);a1.add(0);a1.add(0);a1.add(0);a.add(a1);
		System.out.println(r);
		System.out.println(a);
	}
}