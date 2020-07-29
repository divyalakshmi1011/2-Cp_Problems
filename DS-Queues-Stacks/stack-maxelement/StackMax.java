import java.util.*;

public class StackMax {
    static Stack<Integer> stack;
    static Stack<Integer> track;
    StackMax() {
        stack = new Stack<Integer>();
        track = new Stack<Integer>();
    }
    public static void push(int a) {
        stack.push(a);
        if(stack.size() == 1) {
            track.push(a);
        } else {
            int temp = track.peek();
            if(a > temp) {
                track.push(a);
            } else {
                track.push(temp);
            }
        }
    }
    public static int pop(){
        int p = stack.pop();
        track.pop();
        return p;
    }
    public static int getMax(){
        int m = track.peek();
        return m;
    }
    public static void main(String[] args) {
        StackMax s = new StackMax();
        s.push(1);
        s.push(2);
        s.push(3);
        s.push(4);
        s.push(5);
        s.push(6);
        System.out.println(s.getMax());
    }
}