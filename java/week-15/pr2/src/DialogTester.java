import javax.swing.*;
import java.awt.*;

public class DialogTester extends JDialog {

    public DialogTester() {
        setSize(300, 200);
        setTitle("다이얼로그 테스터");
        this.setModal(true);
        makeUI();
        setVisible(true);
    }

    public void makeUI() {
        setLayout(new GridLayout(1, 2));
        add(new JLabel("연습용"));
        add(new JButton("버튼"));
    }

    public static void main(String[] args) {
        /*
         * new DialogTester();
         * System.out.println("프로그램");
         */

        /*
         * String str = JOptionPane.showInputDialog("이름을 입력하세요 : ");
         * 
         * if (str != null) {
         * System.out.println(str);
         * } else {
         * System.out.println("취소");
         * }
         */

        /*
         * int n = JOptionPane.showConfirmDialog(null, "계속 진행할까요?", "결정",
         * JOptionPane.YES_NO_OPTION);
         * if (n == JOptionPane.YES_OPTION) {
         * System.out.println("계속 진행");
         * } else {
         * System.out.println("중단");
         * }
         */

        JOptionPane.showMessageDialog(null, "불났음", "불",
                /* JOptionPane.INFORMATION_MESSAGE */JOptionPane.WARNING_MESSAGE);
    }
}
