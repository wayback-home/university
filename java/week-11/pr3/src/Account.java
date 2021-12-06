import java.io.DataOutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class Account {

    public static void main(String[] args) {
        try {
            FileOutputStream fos = new FileOutputStream("account.bin");
            DataOutputStream dos = new DataOutputStream(fos);

            getset setBalance = new getset();
            setBalance.setAccount();

            for (int j = 0; j < 10; j++) {
                dos.writeInt(setBalance.getBalance(j));
                System.out.println(setBalance.getBalance(j));
            }

            dos.close();
            System.out.println("완료");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        } catch (IOException e) {

            e.printStackTrace();
        }
    }
}
