public class Tester {
    public static void main(String[] args) {
        IntArray array = new IntArray(10);
        int i;
        for (i = 0; i < array.getLength(); i++) {
            System.out.println(array.get(i));
        }
        System.out.println("Total : " + array.getTotal());
        System.out.println("Sub Total : " + array.getTotal(1, 4));
    }
}