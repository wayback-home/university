import java.util.Set;

public class Person {
    int age;

    public void set(int n) {
        age = n;
    }

    public int get() {
        return age;
    }

    public static void main(String[] args) {
        Person lee = new Person();

        lee.set(20);
        System.out.println(lee.get());

        lee.set(22);
        System.out.println(lee.get());
    }
}
