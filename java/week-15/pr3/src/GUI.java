import java.util.Vector;
import javax.swing.*;

public class GUI extends JFrame {
    private Vector<Account> accounts;
    private Account target;

    public GUI() {
        accounts = new Vector<Account>();

        setSize(800, 600);
        setTitle("계좌");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);

        makeMenu();
        makeUI();

        setVisible(true);

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

        accMemu.add(generateMenu);

        mb.add(accMenu);
        mb.add(quitMenu);

        this.setJMenuBar(mb);

    }

    public void newAccount() {
        String str = JOptionPane.showInputDialog(null, "초기 예금액을 입력하시오 : ");
        int amount;
        if (str == null) {
            amount = 0;
        } else {
            amount = Integer.valueOf(str);
        }
        target = new Account(amount);
        accounts.add(target);
    }

    public void makeUI() {

    }

    public static void main(String[] args) {
        new GUI();
    }
}
