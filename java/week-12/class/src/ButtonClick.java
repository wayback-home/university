import java.awt.event.*;

public class ButtonClick implements ActionListener {

    public void actionPerformed(ActionEvent e) {
        System.out.println("Button is clicked(Outer Class).");

        System.exit(0);
    }

}