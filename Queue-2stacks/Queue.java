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
        while(!s1.empty()) {
            int temp = s1.pop();
            // System.out.println("temp" + temp);
            s2.push(temp);
        }
        int p = s2.pop();
        while(!s2.empty()) {
            int temp = s2.pop();
            // System.out.println("temp" + temp);
            s1.push(temp);
        }
        return p;
    }
    public static void main(String[] args) {
        push(1);
        push(2);
        push(3);
        System.out.println(pop());
        push(4);
        push(5);
        push(6);
        System.out.println(pop());
        System.out.println(pop());
        System.out.println(pop());
    }
}