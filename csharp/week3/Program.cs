using System;

namespace week3
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 0;
            int y = 0;
            int whichLeftRight = 0;
            string toRight = "m@~ 뿌우~";
            string toLeft = "~뿌우 ~@m";
            bool state = true;


            Console.WriteLine("방향키로 코끼리를 이동시키세요");
            Console.WriteLine("이동범위 : 가로 100, 세로 100");
            Console.WriteLine("종료 : Enter 키");



            while (state)
            {
                ConsoleKeyInfo info = Console.ReadKey();
                Console.Clear();
                
                if (info.Key == ConsoleKey.UpArrow){
                    
                    y -=1;


                    if (y <0)
                    {   
                        Console.WriteLine("더 이상 위로 움직일 수 없습니다");
                        y = 0;
                    }
                    else
                    {
                        Console.SetCursorPosition(x,y);
                        if(whichLeftRight == 0){
                            Console.WriteLine(toRight);
                        }
                        else
                        {
                            Console.WriteLine(toLeft);
                        }
                    }

                }

                else if(info.Key == ConsoleKey.RightArrow){
                    x +=1;
                    Console.Clear();

                    if (x >100)
                    {
                        Console.WriteLine("더 이상 오른쪽으로 움직일 수 없습니다.");
                        x = 100;
                    }
                    else
                    {
                        whichLeftRight = 0;
                        Console.SetCursorPosition(x,y);
                        if(whichLeftRight == 0){
                            Console.WriteLine(toRight);
                        }
                        else
                        {
                            Console.WriteLine(toLeft);
                        }
                    }

                }

                else if(info.Key == ConsoleKey.DownArrow){
                    y += 1;
                    Console.Clear();
                    
                    if (y > 100)
                    {
                        Console.WriteLine("더 이상 아래로 움직일 수 없습니다.");
                        y = 100;
                    }
                    else
                    {
                        Console.SetCursorPosition(x,y);
                        if(whichLeftRight == 0){
                            Console.WriteLine(toRight);
                        }
                        else
                        {
                            Console.WriteLine(toLeft);
                        }
                    }

                }

                else if(info.Key == ConsoleKey.LeftArrow){
                    x -= 1;
                    Console.Clear();

                    if (x <0)
                    {
                        Console.WriteLine("더 이상 왼쪽으로 갈 수 없습니다.");
                        x = 0;
                    }
                    else
                    {
                        whichLeftRight = 1;
                        Console.SetCursorPosition(x,y);
                        if(whichLeftRight == 0){
                            Console.WriteLine(toRight);
                        }
                        else
                        {
                            Console.WriteLine(toLeft);
                        }
                    }

                }

                else if(info.Key == ConsoleKey.Enter){
                    state = false;
                    break;
                }
                else
                {
                    Console.Clear();
                    Console.WriteLine("방향키와 엔터 외에는 입력할 수 없습니다.");
                }
            }
        }
    }
}

