import javax.swing.*;
import java.awt.*;

public class GUITester extends JFrame {
    public GUITester() {
        setSize(450, 350);
        setTitle("연습용");
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        makeMenu();
        makeToolbar();
        makeUI();

        setVisible(true);
    }

    public void makeMenu() {
    }

    public void makeToolbar() {
        setLayout(new BorderLayout());
        JToolBar bar = new JToolBar();

        bar.setFloatable(false);
        JButton button = new JButton("exit");
        button.setToolTipText("응용 프로그램 종료");

        bar.add(button);

        this.add(bar, BorderLayout.NORTH);
    }

    public void makeUI() {
        JTabbedPane tab = new JTabbedPane(JTabbedPane.TOP);
        JLabel label = new JLabel("Good");
        JButton button = new JButton("press");

        tab.addTab("라벨", label);
        tab.addTab("버튼", button);

        add(tab);
    }

    public static void main(String[] args) {
        new GUITester();
    }
}
