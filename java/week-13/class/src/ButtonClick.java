import java.awt.event.*;

//step 1. 액션 이벤트를 이벤트를 구현한 클래스
public class ButtonClick implements ActionListener {

    public void actionPerformed(ActionEvent e) {
        System.out.println("Button is clicked(Outer Class).");
        System.exit(0); // 출력 후 종료시킴
    }

}