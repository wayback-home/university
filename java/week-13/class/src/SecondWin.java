import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.GridLayout;
import java.awt.FlowLayout;
import java.awt.BorderLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

//public class SecondWin extends JFrame{
public class SecondWin extends JFrame implements ActionListener {
    private JButton[] buttons;

    public SecondWin() {
        buttons = new JButton[12];
        setTitle("두번째 윈도우");
        setSize(700, 500);
        // this 입력하면 자동완성이 떠서 작성하기 쉬움
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);

        // FlowLayout layout = new FlowLayout();
        // setLayout(layout);
        // 위 두줄과 아래 한 줄은 같은 구문임
        // setLayout(new FlowLayout());

        // setLayout(new GridLayout(4, 3));

        makeUI();
        this.setVisible(true);
    }

    private void makeUI() {

        JPanel northPanel = new JPanel();
        JPanel centerPanel = new JPanel();
        JPanel southPanel = new JPanel();

        northPanel.setLayout(new BorderLayout());
        centerPanel.setLayout(new GridLayout(3, 4));
        southPanel.setLayout(new GridLayout(1, 2));

        add(northPanel, BorderLayout.NORTH);
        add(centerPanel, BorderLayout.CENTER);
        add(southPanel, BorderLayout.SOUTH);

        JLabel label = new JLabel("0");
        northPanel.add(label, BorderLayout.CENTER);

        for (int i = 0; i < 10; i++) {
            buttons[i] = new JButton(String.valueOf(i));
            add(buttons[i]);
        }

        buttons[10] = new JButton("+");
        // add(buttons[10], BorderLayout.NORTH);
        centerPanel.add(buttons[10]);
        buttons[11] = new JButton("=");
        // add(buttons[11], BorderLayout.SOUTH);
        northPanel.add(buttons[11]);

        // step 2.
        // ButtonClick click = new ButtonClick();
        ButtonHandler click = new ButtonHandler();

        // ActionListener는 인터페이스라 위처럼 선언할 수 없음
        // ActionListener click = new ActionListener();

        // step 3.

        // 아래는 buttons[11] << "="키를 클릭했을 때 발생하는 이벤트임

        // (1)
        // Outer Class 혹은 Inner Class 출력 (34줄 활성화시 Outer, 35줄은 Inner)
        // buttons[11].addActionListener(click);

        // (2)
        // 안에 넣은 값을 출력함 (Annonymouse Class)
        // buttons[11].addActionListener(new ActionListener() {
        // public void actionPerformed(ActionEvent e) {
        // System.out.println("Button is clicked(Annonymouse Class).");
        // System.exit(0);
        // }
        // });

        // (3)
        // 80줄대에 있는 클래스를 출력함 (This Class)
        buttons[11].addActionListener(this);

        southPanel.add(new JButton("버튼 1"));
        southPanel.add(new JButton("버튼 2"));

    }

    public static void main(String[] args) {
        // 만든 GUI를 띄워줌
        SecondWin win = new SecondWin();

    }

    // step 1.
    class ButtonHandler implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            System.out.println("Button is clicked(Inner Class).");
            System.exit(0); // 출력 후 종료시킴
        }

    }

    // public class SecondWin extends JFrame implements ActionListener에서
    // implements ActionListener를 해결하기 위한 클래스
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("Button is clicked(This Class).");
        System.exit(0);

    }

}