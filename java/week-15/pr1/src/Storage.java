public class Storage<T> {
    private T data;

    public Storage(T d) {
        data = d;
    }

    public void set(T d) {
        data = d;
    }

    public T get() {
        return data;
    }
}