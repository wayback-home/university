﻿using System;
using System.Collections.Generic;

namespace test
{
    class Program
    {
        class Animal
        {
            public virtual void Eat()
            {
                Console.WriteLine("냠냠 먹습니다");
            }
        }
        class Dog : Animal
        {
            public override void Eat()
            {
                Console.WriteLine("강아지 사료를 먹습니다");
            }


        }
        class Cat : Animal
        {
            public override void Eat()
            {
                Console.WriteLine("고양이 사료를 먹습니다");
            }
        }
        static void Main(string[] args)
        {
            List<Animal> Animals = new List<Animal>(){
                new Dog(), new Cat(), new Dog(), new Cat(),
                new Dog(), new Cat(),new Dog(), new Cat(),
            };

            foreach (var item in Animals)
            {
                item.Eat();
            }
        }
    }
}
