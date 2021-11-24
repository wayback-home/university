using System;

namespace pr6
{
    delegate void MyDelegate(int a, int b);
    class Program
    {
        public static void Calculator(int a, int b, MyDelegate dele)
        {
            dele(a, b);
        }

        public static void Add(int a, int b)
        {
            Console.WriteLine(a + " + " + b + " = " + (a + b));
        }
        public static void Sub(int a, int b)
        {
            Console.WriteLine(a + " - " + b + " = " + (a - b));
        }
        static void Main(string[] args)
        {
            MyDelegate Plus = new MyDelegate(Add);
            MyDelegate Minus = new MyDelegate(Sub);

            Calculator(5, 10, Plus);
            Calculator(5, 10, Minus);
        }
    }
}
