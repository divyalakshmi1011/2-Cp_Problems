class A {
    static int add(int i, int j) {
        return (i + j);
    }
}
public class B  {
    public static void main (String[] args) {
        int mask = 0x000F;
        int value = 0x2222;
        System.out.println(value & mask);
    }
}