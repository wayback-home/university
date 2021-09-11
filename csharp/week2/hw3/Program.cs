using System;

namespace hw3
{
    class Program
    {
        static void Main(string[] args)
        {
            string r;
            double rC, round, area;
            var pi = 3.14;
            Console.WriteLine("원 둘레와 넓이 구하기 프로그램");
            Console.WriteLine("반지름을 입력하세요");
            r = Console.ReadLine();
            rC = Convert.ToDouble(r);
            round = 2 * pi * rC;
            area = pi * rC * rC;

            Console.WriteLine("둘레 = {0}",round);
            Console.WriteLine("넓이 = {0}",area);
            
        }
    }
}
