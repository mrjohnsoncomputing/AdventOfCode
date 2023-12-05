using PuzzleSolutions.Database;
using PuzzleSolutions.Database.Model;
using PuzzleSolutions.Extensions;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions
{
    public class Day4Puzzle : IPuzzleDay
    {
        public string SolvePart1()
        {
            using var dbContext = new Aoc2023DbContext();
            var result = dbContext.Day4?
                .ToList()
                .Select(scratchcard => scratchcard.CalculatePoints())
                .Sum();

            return $"{result}";
        }

        public string SolvePart2()
        {
            using var dbContext = new Aoc2023DbContext();
            var scratchcards = dbContext.Day4?
                .ToList()
                .Select(scratchcard => scratchcard.PopulateMatchingNumberCount())
                .ToList();

            var total = 0;
            foreach (var scratchcard in scratchcards!)
            {
                total++;
                scratchcard.Print();
                total += GetScratchCards(scratchcards, scratchcard);
            }

            return $"{total}";
        }

        public int GetScratchCards(List<Scratchcard> scratchcards, Scratchcard scratchcard, int level = 0)
        {
            var total = 0;
            PrintLevel(level, scratchcard.Id ,scratchcard.MatchingNumbers);
            if (scratchcard.MatchingNumbers == 0) return 0;

            for (var i = scratchcard.Id; i < scratchcard.Id + scratchcard.MatchingNumbers; i++)
            {
                total++;
                if (i >= scratchcards.Count()) break;

                var additionalCard = scratchcards[i];

                total += GetScratchCards(scratchcards, additionalCard, level+1);
            }
            return total;
        }

        public void PrintLevel(int level, int id, int matchingNumbers)
        {
            var indent = " ";
            var message = string.Empty;
            for (var i = 0; i<level; i++)
            {
                message += indent;
            }
            message += $"[{id}] Level {level}: {matchingNumbers} matches";
            Console.WriteLine(message);
        }
    }
}
