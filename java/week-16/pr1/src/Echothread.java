import java.net.Socket;
import java.io.*;

public class Echothread extends Thread {
    private Socket socket;

    public Echothread(Socket sock) {
        socket = sock;
    }

    @Override
    public void run() {
        super.run();
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));

            String str;
            while (true) {

                str = reader.readLine();
                System.out.println("From client : " + str);
                writer.write(str + "\n");
                writer.flush();
                if (str.equals("exit")) {
                    break;
                }
            }
        } catch (IOException e) {
        }

        try {
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
