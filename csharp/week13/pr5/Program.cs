using System;

namespace pr5
{
    public delegate void TestDelegate();
    class Program
    {
        static void TestMethod()
        {
            Console.WriteLine("델리게이터 실행");
        }

        static void Main(string[] args)
        {
            TestDelegate delegateA = TestMethod;
            TestDelegate delegateB = delegate ()
            {
                Console.WriteLine("무명 델리게이터 실행");
            };
            TestDelegate delegateC = () =>
            {
                Console.WriteLine("람다 델리게이터 실행");
            };

            delegateA();
            delegateB();
            delegateC();
        }
    }
}
