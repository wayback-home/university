using System;

namespace pr7
{
    class Program
    {
        public delegate void SendString(string msg);

        public static void Hello(string msg)
        {
            Console.WriteLine("헬로~~" + msg);
        }
        public static void Goodbye(string msg)
        {
            Console.WriteLine("굿바이~" + msg);
        }

        static void Main(string[] args)
        {
            SendString sayHello, sayGoodbye, multiDelegate;

            sayHello = Hello; sayHello("여러분");
            sayGoodbye = Goodbye; sayGoodbye("여러분");

            multiDelegate = sayHello + sayGoodbye;
            multiDelegate("홍길동");

            multiDelegate -= sayGoodbye;
            multiDelegate("임꺽정");
        }
    }
}
