import java.net.Socket;
import java.util.Scanner;
import java.io.*;

public class ChatAgent {
    private Socket socket;

    public ChatAgent(Socket sock) {
        socket = sock;
    }

    public void begin() {
        try {
            new Th().start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            String str;

            while (true) {
                str = reader.readLine();
                if (str == null || str.equals("exit")) {
                    break;
                }
                System.out.println("Peer >> " + str);
            }
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    class Th extends Thread {

        @Override
        public void run() {
            super.run();
            Scanner in = new Scanner(System.in);
            String str;
            try {
                BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));

                while (true) {
                    str = in.nextLine();

                    if (socket.isConnected()) {
                        writer.write(str + "\n");
                        writer.flush();
                    } else {
                        break;
                    }
                    if (str.equals("exit")) {
                        break;
                    }
                }

            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }
}
