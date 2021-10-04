using System;

namespace _07
{
    class Program
    {


        public class Person
        {
            public string name = "윤인성";
            public string address = "서울특별시 강서구";
            
            return name
            return address
            Pet()
        }

        public class Pet
        {
            public string name {get;set;}
            public int age {get; set;}

            public string returnPet()
            {
                return "이름 : " + name + "\t나이 : " + age;
            }
        }



        static void Main(string[] args)
        {
    
            List<Pet> pets = new List<Pet>();
            pets.Add(new Pet() {name="구름", age=7});
            pets.Add(new Pet() {name="별", age=1});


            Console.WriteLine(Person());
        }
    }
}
