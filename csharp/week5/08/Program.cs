using System;

namespace _08
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            int num = random.Next(0,1000);

            
            int a;
            while (true)
            {
                Console.WriteLine("숫자를 입력해주세요 : ");
                string sNum = Console.ReadLine();
                a = Convert.ToInt32(sNum);
                if (a == num)
                {
                    Console.WriteLine("맞췄습니다.");
                    break;
                }
                else if (a>num)
                {
                    Console.WriteLine("더 작습니다.");
                }
                else if (a<num)
                {
                    Console.WriteLine("더 큽니다.");
                }
            }

        }
    }
}
