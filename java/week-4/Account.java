//예제 2번 4번
public class Account {

    int cusNum;
    int money;

    public Account() {
        cusNum = 99;
        money = 0;
    }

    public Account(int person, int b) {
        cusNum = person;
        money = b;
    }

    public void save(int person, int n) {
        money = money + n;
    }

    public void use(int person, int n) {
        money = money - n;
    }

    public int chk(int person) {
        return money;
    }

    public int chkuser() {
        return cusNum;
    }

    public static void main(String[] args) {
        Account bank = new Account(88, 1000);
        System.out.println(bank.chkuser());

        System.out.println(bank.chk(88));
    }

}
