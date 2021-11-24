using System;
using System.Collections.Generic;

namespace pr4
{
    class Program
    {
        class Product
        {
            public string Name { get; set; }
            public int Price { get; set; }

        }

        static void Main(string[] args)
        {
            List<Product> products = new List<Product>(){
                new Product() { Name = "감자", Price = 500},
                new Product() { Name = "사과", Price = 700},
                new Product() { Name = "상추", Price = 300}
            };
            products.Sort((a, b) =>
            {
                return a.Price.CompareTo(b.Price);
            });
            foreach (var item in products)
            {
                Console.WriteLine(item.Name + " : " + item.Price);
            }
        }
    }
}
