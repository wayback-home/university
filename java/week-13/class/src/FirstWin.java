import javax.swing.*;

public class FirstWin {

    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setTitle("First Window");
        frame.setSize(500, 350);

        // 창을 닫으면 완전히 프로그램이 종료되게 함
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // 창을 띄워줌
        frame.setVisible(true);

    }

}