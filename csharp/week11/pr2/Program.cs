using System;

namespace pr2
{
    class Program
    {
        class PointClass{
            public int x;
            public int y;

            public PointClass(int x, int y){
                this.x = x;
                this.y = y;
            }

        }
        struct PointStruct{
            public int x;
            public int y;

            public PointStruct(int x, int y){
                this.x = x;
                this.y = y;
            }
        }
        static void Main(string[] args) //! 활용1
        {
            PointClass pointClassA = new PointClass(10, 20); 
            PointClass pointClassB = pointClassA;

            Console.WriteLine("pointClassA : " + pointClassA.x + ", "+pointClassA.y);
            Console.WriteLine("pointClassB : " + pointClassB.x + ", "+pointClassB.y);

            PointStruct pointStructA = new PointStruct(10, 20);
            PointStruct pointStructB = pointStructA;

            Console.WriteLine("pointStructA : " + pointStructA.x + ", "+pointStructA.y);
            Console.WriteLine("pointStructB : " + pointStructB.x + ", "+pointStructB.y);


        }

        /* static void Main(string[] args){ //! 활용2
            PointClass pointClassA = new PointClass(10,20);
            PointClass pointClassB = pointClassA;

            pointClassB.x = 100;
            pointClassB.y = 200;

            Console.WriteLine("pointClassA : "+pointClassA.x +", "+pointClassA.y );
            Console.WriteLine("pointClassB : "+pointClassB.x +", "+pointClassB.y );


            PointStruct pointStructA = new PointStruct(10, 20);
            PointStruct pointStructB = pointStructA;

            pointStructB.x = 100;
            pointStructB.y = 200;

            Console.WriteLine("pointStructA : "+pointStructA.x +", "+pointStructA.y );
            Console.WriteLine("pointStructB : "+pointStructB.x +", "+pointStructB.y );
        } */
    }
}
