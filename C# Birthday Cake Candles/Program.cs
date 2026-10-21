public class Program
{
    public int birthdayCakeCandles()
    {
        Console.WriteLine("Mum sayıları giriniz.");     
        List<int> candles = Console.ReadLine().TrimEnd().Split(' ').Select(int.Parse).ToList();

        int maxTall = 0;
        int counter = 0;

        for (int i = 0; i < candles.Count; i++)
        {
            if (maxTall < candles[i])
            {
                maxTall = candles[i];
                counter = 1;
            }
            else if (candles[i] == maxTall)
            {
                counter++;
            }
            
        }
        return counter;
    }

}




