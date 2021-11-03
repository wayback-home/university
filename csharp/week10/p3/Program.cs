using System;

namespace p3
{
    class DataStore
    {
        public string[] strArr = new string[3];

        public string this[int index]
        {
            get
            {
                return strArr[index];
            }
            set
            {
                strArr[index] = value;
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            DataStore strStore = new DataStore();
            strStore[0] = "One";
            strStore[1] = "Two";
            strStore[2] = "Three";

            for (int i = 0; i < strStore.strArr.Length; i++)
            {
                Console.WriteLine(strStore[i]);
            }
        }
    }
}
