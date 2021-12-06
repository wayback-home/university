import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SecondWin extends JFrame {
    String newtext;
    int flag = 0;
    int total = 0;

    public SecondWin() {

        BorderLayout layout = new BorderLayout();

        JPanel panel = new JPanel();
        JLabel label = new JLabel(" ", JLabel.RIGHT);

        JButton[] btns = new JButton[12];

        ActionListener li = new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Success");
                if (flag == 3) {
                    if (e.getActionCommand().equals("1") || e.getActionCommand().equals("2")
                            || e.getActionCommand().equals("3") || e.getActionCommand().equals("4")
                            || e.getActionCommand().equals("5") || e.getActionCommand().equals("6")
                            || e.getActionCommand().equals("7") || e.getActionCommand().equals("8")
                            || e.getActionCommand().equals("9") || e.getActionCommand().equals("0")) {
                        flag = 0;
                        label.setText(" ");
                        total = 0;
                    }
                }

                if (flag == 4) {
                    flag = 0;
                    total = 0;
                    label.setText(" ");
                }
                String b = e.getActionCommand();

                if (b.equals("0") || b.equals("1") || b.equals("2") || b.equals("3") || b.equals("4") || b.equals("5")
                        || b.equals("6") || b.equals("7") || b.equals("8") || b.equals("9")) {
                    total += Integer.parseInt(e.getActionCommand());
                    flag++;

                    String oldtext = label.getText();
                    String newtext = oldtext + b;
                    label.setText(newtext);

                    if (flag == 2) {
                        flag = 4;
                        label.setText("이 계산기는 한 자리 숫자만 더할 수 있습니다.");

                    }
                } else if (b == "+") {
                    flag = 0;
                    String oldtext = label.getText();
                    String newtext = oldtext + b;
                    label.setText(newtext);
                } else {
                    flag = 3;

                    label.setText(String.valueOf(total));

                }

            }

        };

        label.setFont(new Font("Serif", Font.BOLD, 20));
        label.setOpaque(true);
        label.setBackground(Color.ORANGE);

        for (int i = 0; i < 10; i++) {
            btns[i] = new JButton(String.valueOf(i));
        }
        btns[10] = new JButton("+");
        btns[11] = new JButton("=");

        setTitle("실습 과제3번 계산기");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setLayout(layout);
        panel.setLayout(new GridLayout(4, 3, 25, 15));

        for (int i = 1; i < 4; i++) {
            panel.add(btns[i], BorderLayout.CENTER);
        }
        for (int i = 4; i < 7; i++) {
            panel.add(btns[i], BorderLayout.CENTER);
        }
        for (int i = 7; i < 10; i++) {
            panel.add(btns[i], BorderLayout.CENTER);
        }
        panel.add(btns[10], BorderLayout.CENTER);
        panel.add(btns[0], BorderLayout.CENTER);
        panel.add(btns[11], BorderLayout.CENTER);

        add(label, BorderLayout.NORTH);
        add(panel, BorderLayout.CENTER);

        for (int i = 0; i < btns.length; i++) {
            btns[i].addActionListener(li);
        }

        setVisible(true);
    }

    public static void main(String[] args) {
        SecondWin C = new SecondWin();
    }

}