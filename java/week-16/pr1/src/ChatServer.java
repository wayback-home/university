import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class ChatServer {

    private int port;

    public ChatServer(int p) {
        port = p;
    }

    public void start() {
        try {
            ServerSocket serverSocket = new ServerSocket(port);

            Socket socket = serverSocket.accept();

            ChatAgent agent = new ChatAgent(socket);
            agent.begin();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        ChatServer server = new ChatServer(12345);
        server.start();
    }
}
