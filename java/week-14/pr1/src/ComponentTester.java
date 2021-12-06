import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.ButtonGroup;
import javax.swing.ImageIcon;
import javax.swing.JCheckBox;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import java.awt.GridLayout;

public class ComponentTester extends JFrame {

    public ComponentTester() {
        setTitle("GUI 테스트");
        setSize(400, 350);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);

        makeMenu();
        // makeUI2();
        makeGraphics();

        setVisible(true);
    }

    public void makeUI() {
        // JLabel slbl = new JLabel("Good Morning", SwingConstants.CENTER);
        // JTextField slbl = new JTextField("Good Morning");
        JCheckBox slbl = new JCheckBox("Good Morning");

        // JLabel clbl = new JLabel(new ImageIcon("starbucks.png"));
        JCheckBox clbl = new JCheckBox(new ImageIcon("starbucks.png"));
        clbl.setSelectedIcon(new ImageIcon("heart.png"));
        clbl.addItemListener(new ItemListener() {

            @Override
            public void itemStateChanged(ItemEvent e) {
                if (e.getStateChange() == ItemEvent.SELECTED) {
                    System.out.println("선택");
                } else {
                    System.out.println("해제");
                }
            }

        });

        // JLabel sslbl = new JLabel("My Picture", new ImageIcon("heart.png"),
        // SwingConstants.CENTER);

        setLayout(new BorderLayout());
        add(slbl, BorderLayout.NORTH);
        add(clbl, BorderLayout.CENTER);
        // add(sslbl, BorderLayout.CENTER);

    }

    public void makeUI2() {
        setLayout(new GridLayout(3, 1));
        JRadioButton rb1 = new JRadioButton("국어");
        JRadioButton rb2 = new JRadioButton("영어");
        JRadioButton rb3 = new JRadioButton("수학");
        ButtonGroup bg = new ButtonGroup();
        bg.add(rb1);
        bg.add(rb2);
        bg.add(rb3);

        rb1.addItemListener(new ItemListener() {

            @Override
            public void itemStateChanged(ItemEvent e) {
                if (e.getStateChange() == ItemEvent.SELECTED) {
                    System.out.println("국어 선택");
                } else {
                    System.out.println("국어 해제");
                }
            }

        });

        add(rb1);
        add(rb2);
        add(rb3);
    }

    public void makeMenu() {
        JMenuBar mb = new JMenuBar();
        JMenu fileMenu = new JMenu("File");
        JMenuItem quitMenuItem = new JMenuItem("종료");
        JMenuItem openMenuItem = new JMenuItem("열기");

        quitMenuItem.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }

        });

        openMenuItem.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser fc = new JFileChooser();
                fc.showOpenDialog(null);
            }
        });

        fileMenu.add(openMenuItem);
        fileMenu.add(quitMenuItem);
        mb.add(fileMenu);
        this.setJMenuBar(mb);
    }

    public void makeGraphics() {
        myPanel panel = new myPanel();
        add(panel);
    }

    public static void main(String[] args) {
        new ComponentTester();

    }
}
