using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            int timeForPhoto = int.Parse(Console.ReadLine());
            int sceni = int.Parse(Console.ReadLine());  
            int timeForScena = int.Parse(Console.ReadLine());

            double podgotovka = timeForPhoto * 0.15;
            double timeForSteaming = sceni * timeForScena;
            double time = podgotovka + timeForSteaming;
            
            if(timeForPhoto > time)
            {
                Console.WriteLine($"You managed to finish the movie on time! You have {Math.Ceiling(timeForPhoto - time)} minutes left!");
            }
            else
            {
                Console.WriteLine($"Time is up! To complete the movie you need {Math.Ceiling(time - timeForPhoto)} minutes.");
            }
        }
    }
}