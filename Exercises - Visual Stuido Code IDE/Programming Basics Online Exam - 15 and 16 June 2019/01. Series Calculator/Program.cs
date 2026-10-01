using System;

namespace _01._
{
    class Program
    {
        static void Main(string[] args)
        {
            string nameOfSerial = Console.ReadLine();
            int season = int.Parse(Console.ReadLine());
            int episode = int.Parse(Console.ReadLine());
            double minute = double.Parse(Console.ReadLine());

            double reklama = 0.2 * minute;
            double epizodeWithReklama = minute + reklama;
            double specialEpizode = season * 10;
            double fullTime = epizodeWithReklama * episode * season + specialEpizode;

            Console.WriteLine($"Total time needed to watch the {nameOfSerial} series is {Math.Ceiling(fullTime)} minutes.");
        }
    }
}