using PuzzleSolutions.Extensions;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.Model
{
    public class Scratchcard : GenericDbModel
    {
        public Scratchcard() { }

        public Scratchcard(string winningNumbers, string playingNumbers)
        {
            WinningNumberString = winningNumbers;
            PlayingNumberString = playingNumbers;
        }

        public string WinningNumberString { get; private set; }
        public string PlayingNumberString { get; private set; }

        public List<int>? WinningNumbers { get; private set; }
        public List<int>? PlayingNumbers { get; private set; }

        public int MatchingNumbers { get; private set; }

        private void PopulateLists()
        {
            WinningNumbers = WinningNumberString
                    .Split(" ")
                    .ConvertToIntArray()
                    .ToList();

            PlayingNumbers = PlayingNumberString
                .Split(" ")
                .ConvertToIntArray()
                .ToList();
        }

        public Scratchcard PopulateMatchingNumberCount()
        {
            PopulateLists();
            var matches = PlayingNumbers!
                .Where(number => WinningNumbers!.Contains(number));
            MatchingNumbers = matches.Count();
            return this;
        }

        public double CalculatePoints()
        {
            PopulateMatchingNumberCount();

            if (MatchingNumbers <= 0) return 0;

            var result = Math.Pow(2, MatchingNumbers - 1);
            return result;
        }

        public void Print()
        {
            Console.WriteLine($"Scratchcard {Id}");
            Console.WriteLine($"Winning Numbers: {WinningNumbers?.Stringify()}");
            Console.WriteLine($"Playing Numbers: {PlayingNumbers?.Stringify()}");
            Console.WriteLine($"Matching Numbers: {MatchingNumbers}\n");
        }
    }
}
