public class Main {
    public static void main(String[] args) {
        Storage<String> d = new Storage<String>("Good");
        // Storage<String> d = new Storage<>("Good");
        // var d = new Storage<String>("Good");

        System.out.println(d.get());

        Storage<Integer> d2 = new Storage<Integer>(Integer.valueOf(99));
        System.out.println(d2.get());
    }
}
