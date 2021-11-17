import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

public class inputTest {

    public static void main(String[] args) {

        Object[] obj = new Object[10];

        try {
            FileInputStream fis = new FileInputStream("test1.dat");

            ObjectInputStream ois = new ObjectInputStream(fis);

            for (int i = 0; i < 10; i++) {
                obj[i] = ois.readObject();
            }

            for (int j = 0; j < 10; j++) {
                System.out.println(obj[j].toString());
            }
            ois.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

    }
}
