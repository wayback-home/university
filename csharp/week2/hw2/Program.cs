using System;

namespace hw2
{
    class Program
    {
        static void Main(string[] args)
        {
            string kg;
            double kgC, lb;
            Console.WriteLine("kg to lb Program");
            Console.WriteLine("write kg");
            kg = Console.ReadLine();
            kgC = Convert.ToDouble(kg);
            lb = 2.20462262 * kgC;

            Console.WriteLine("{0}kg = {1}lb",kg,lb);
        }
    }
}
