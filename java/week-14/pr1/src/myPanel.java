import java.awt.Graphics;
import java.awt.Color;
import java.awt.Font;
import javax.swing.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

public class myPanel extends JPanel implements MouseListener {
    private int x, y;

    public myPanel() {
        x = y = -1;
        this.addMouseListener(this);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLUE);
        g.setFont(new Font("명조", Font.BOLD, 32));
        g.drawOval(50, 50, 100, 100);

        g.setColor(Color.RED);
        g.drawString("CIRCLE", 50, 100);

        g.drawRoundRect(50, 50, 100, 100, 10, 10);
        g.drawArc(50, 50, 100, 100, 45, 180);
        g.fillArc(50, 50, 100, 100, 0, 45);
        g.setColor(Color.GREEN);
        g.fillArc(55, 35, 100, 100, 45, 70);
        g.setColor(Color.BLUE);
        g.fillArc(50, 50, 100, 100, 115, 90);
        g.setColor(Color.MAGENTA);
        g.fillArc(50, 50, 100, 100, 205, 155);

        if (x >= 0) {
            g.fillOval(x - 5, y - 5, 10, 10);
        }

    }

    @Override
    public void mouseClicked(MouseEvent e) {
        x = e.getX();
        y = e.getY();
        repaint();
    }

    @Override
    public void mouseEntered(MouseEvent e) {

    }

    @Override
    public void mouseExited(MouseEvent e) {

    }

    @Override
    public void mousePressed(MouseEvent e) {

    }

    @Override
    public void mouseReleased(MouseEvent e) {

    }

}
