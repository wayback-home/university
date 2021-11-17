import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class outputTest {
    public static void main(String[] args) {
        try {
            FileOutputStream fos = new FileOutputStream("test1.dat");
            ObjectOutputStream oos = new ObjectOutputStream(fos);

            getset setBalance = new getset();
            setBalance.setAccount();

            for (int i = 0; i < 10; i++) {
                oos.writeObject(setBalance.getBalance(i));
                System.out.println(setBalance.getBalance(i));
            }
            System.out.println("완료");

            oos.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
