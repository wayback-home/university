using System;

namespace p2
{
    class DataStore<T>
    {
        public T[] data = new T[2];
        public void AddOrUpdate(int index, T item)
        {
            if (index >= 0 && index < 2)
            {
                data[index] = item;
            }
        }

        public T GetData(int index)
        {
            if (index >= 0 && index < 2)
            {
                return data[index];
            }
            else
            {
                return default(T);
            }
        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            DataStore<string> fruits = new DataStore<string>();
            fruits.AddOrUpdate(0, "Apple");
            fruits.AddOrUpdate(1, "Orange");

            Console.WriteLine(fruits.GetData(0));
            Console.WriteLine(fruits.GetData(1));
            Console.WriteLine(fruits.GetData(2));


            DataStore<int> price = new DataStore<int>();
            price.AddOrUpdate(0, 50);
            price.AddOrUpdate(1, 65);
            price.AddOrUpdate(2, 100);

            Console.WriteLine(price.GetData(0));
            Console.WriteLine(price.GetData(1));
            Console.WriteLine(price.GetData(2));
        }
    }
}
