import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Vector;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JTabbedPane;
import javax.swing.JToolBar;

public class GUI extends JFrame {
    private Vector<Account> accounts;
    private Account target;

    public GUI() {
        accounts = new Vector<Account>();
        target = null;

        setSize(450, 350);
        setTitle("연습용");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);

        makeMenu();
        makeToolBar();
        makeUI();

        setVisible(true);
    }

    public void makeToolBar() {
        setLayout(new BorderLayout());
        JToolBar bar = new JToolBar();
        bar.setFloatable(false);
        JButton button = new JButton("exit");
        button.setToolTipText("응용 프로그램 종료");

        bar.add(button);

        this.add(bar, BorderLayout.NORTH);
    }

    public void makeMenu() {
        JMenuBar mb = new JMenuBar();
        JMenu accMenu = new JMenu("Account");
        JMenuItem quitMenu = new JMenuItem("종료");
        quitMenu.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });

        JMenuItem generateMenu = new JMenuItem("생성");
        generateMenu.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                newAccount();
            }
        });

        accMenu.add(generateMenu);

        JMenuItem checkMenu = new JMenuItem("잔액확인");
        checkMenu.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                checkAccount();
            }

        });

        accMenu.add(checkMenu);

        mb.add(accMenu);
        mb.add(quitMenu);

        this.setJMenuBar(mb);
    }

    public void checkAccount() {
        JOptionPane.showMessageDialog(null, "현재 잔액은 " + target.get() + "입니다.",
                "잔액확인", JOptionPane.INFORMATION_MESSAGE);
    }

    public void newAccount() {
        String str = JOptionPane.showInputDialog(null, "초기 예금액을 입력하시오:");
        int amount;
        if (str == null)
            amount = 0;
        else
            amount = Integer.valueOf(str);
        target = new Account(amount);
        accounts.add(target);

    }

    public void makeUI() {
        JTabbedPane tab = new JTabbedPane(JTabbedPane.BOTTOM);

        JLabel label = new JLabel("good");
        JButton button = new JButton("press");

        tab.addTab("라벨", label);
        tab.addTab("버튼", button);

        add(tab);
    }

    public static void main(String[] args) {
        new GUI();
    }

}
