import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;
import java.io.*;

public class ChatClient {
    private String ipadder;
    private int port;

    public ChatClient(String ip, int p) {
        ipadder = ip;
        port = p;

    }

    public void start() {
        Scanner in = new Scanner(System.in);
        String str;
        Socket socket;

        try {
            socket = new Socket(ipadder, port);

            ChatAgent agent = new ChatAgent(socket);
            agent.begin();

        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        ChatClient client = new ChatClient("localhost", 12345);
        client.start();

    }
}
