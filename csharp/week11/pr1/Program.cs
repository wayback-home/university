using System;

namespace pr1
{
    class Program
    {
        struct PointD{
            public int x;
            public int y;
            public string testA;
            public string testB;

            public PointD(int x, int y){
                this.x = x;
                this.y = y;
                this.testA = "초기화";
                this.testB = "초기화";

            }
            
            public PointD(int x, int y, string test){
                this.x = x;
                this.y = y;
                this.testA = test;
                this.testB = test;
            }
        }
        static void Main(string[] args)
        {
            PointD pd = new PointD();
            // PointD pd = new PointD(10, 20);
            // PointD pd = new PointD(10, 20, "테스트");
            Console.WriteLine(pd.x + ","+pd.y);
            Console.WriteLine(pd.testA + ","+pd.testB);
        }
    }
}
