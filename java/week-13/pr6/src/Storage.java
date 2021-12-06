public class Storage<T> {
    private T obj;

    public void set(T o) {
        obj = o;
    }

    public T get() {
        return obj;
    }
}
