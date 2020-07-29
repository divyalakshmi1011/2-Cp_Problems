import java.util.*;

public class Queue{
    static Stack<Integer> s1 = new Stack<Integer>();
    static Stack<Integer> s2 = new Stack<Integer>();
    Queue() {

    }
    public static void push(int a) {
        s1.push(a);
    }
    public static int pop() {
        Iterator<Integer> it = s1.iterator();
        while(it.hasNext()){
            int temp = it.next();
            s2.push(temp);
        }
        int p = s2.pop();
        return p;
    }
    public static void main(String[] args) {
        push(1);
        push(2);
        push(3);
        System.out.println(pop());
    }
}