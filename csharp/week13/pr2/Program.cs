using System;

namespace pr2
{
    class Program
    {
        delegate void MyDel(string s);

        static void MyMethod(string s)
        {
            Console.WriteLine(s);
        }
        static void Main(string[] args)
        {
            MyDel md = MyMethod;
            Console.WriteLine(md);

            md("라라라");
            md("루루루");
        }
    }
}
