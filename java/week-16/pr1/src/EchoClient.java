import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;
import java.io.*;

public class EchoClient {
    private String ipadder;
    private int port;

    public EchoClient(String ip, int p) {
        ipadder = ip;
        port = p;

    }

    public void start() {
        Scanner in = new Scanner(System.in);
        String str;
        Socket socket;

        try {
            socket = new Socket(ipadder, port);
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));

            while (true) {
                System.out.println("Input string : ");
                str = in.nextLine();
                if (str == null) {
                    continue;
                }

                writer.write(str + "\n");
                writer.flush();

                str = reader.readLine();
                System.out.println("From Server : " + str);

                if (str.equals("exit")) {
                    break;
                }
            }

        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        EchoClient client = new EchoClient("localhost", 12345);
        client.start();

    }
}
