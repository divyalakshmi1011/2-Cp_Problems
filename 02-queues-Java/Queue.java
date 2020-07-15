public class Queue{
	int[] storage = new int[20];
	int front;
	int rear;
	public Queue(int head){
		front = 0;
		rear = 0;
		storage[rear++] = head;
	}
	
	public void enqueue(int new_ele){
			 this.rear = this.rear + 1;
			 storage[rear] = new_ele;
	}

	public int peek(){
		return storage[this.front];
	}

	public int dequeue(){
		int item = this.storage[this.front];
		this.front = this.front + 1; 
		return item;
	}
	public static void main(String[] args) {
		Queue q = new Queue(1);
		q.enqueue(2);
		q.enqueue(3);
		System.out.println(q.dequeue());
	}
}