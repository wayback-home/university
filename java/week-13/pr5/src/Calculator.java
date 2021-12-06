package src;

public class Calculator extends Thread {
    private TotalMain owner;
    int begin;
    int end;

    public Calculator(TotalMain obj, int b, int e) {
        owner = obj;
        begin = b;
        end = e;
    }

    @Override
    public void run() {
        super.run();
        for (int i = begin; i < end; i++) {
            owner.add(i);
        }
    }
}
