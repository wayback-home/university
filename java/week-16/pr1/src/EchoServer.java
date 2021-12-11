import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class EchoServer {

    private int port;

    public EchoServer(int p) {
        port = p;
    }

    public void start() {
        try {
            ServerSocket serverSocket = new ServerSocket(port);

            Socket socket = serverSocket.accept();

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
            socket.close();
            serverSocket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        EchoServer server = new EchoServer(23456);
        server.start();
    }
}
