using System;
using System.Collections.Generic;

namespace pr1
{
    class Program
    {
        class Product : IComparable
        {
            public string Name { get; set; }
            public int Price { get; set; }

            public int CompareTo(object obj)
            {
                return Price.CompareTo((obj as Product).Price);
            }

        }

        static int SortWithPrice(Product a, Product b)
        {
            return a.Price.CompareTo(b.Price);
        }




        static void Main(string[] args)
        {
            List<Product> products = new List<Product>(){
                new Product() { Name = "감자", Price = 500},
                new Product() { Name = "사과", Price = 700},
                new Product() { Name = "포도", Price =300}
            };

            products.Sort(SortWithPrice);
            foreach (var item in products)
            {
                Console.WriteLine(item.Name + " : " + item.Price);
            }
        }
    }
}
