using System;

namespace hw1
{
    class Program
    {
        static void Main(string[] args)
        {
            string inch;
            double inchC, cm;
            Console.WriteLine("inch to cm Program");
            Console.WriteLine("write inch");
            inch = Console.ReadLine();
            inchC = Convert.ToDouble(inch);
            cm = 2.54 * inchC;

            Console.WriteLine("{0}inch = {1}cm",inch,cm);
        }
    }
}
