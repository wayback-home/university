import java.io.IOException;
import java.net.*;
import java.util.*;

public class MEchoServer {
    private int port;

    public MEchoServer(int p) {
        port = p;
    }

    public void start() {
        try {
            ServerSocket ss = new ServerSocket(port);
            Socket socket;

            while (true) {
                socket = ss.accept();
                new Echothread(socket).start();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        MEchoServer server = new MEchoServer(23456);
        server.start();
    }
}
