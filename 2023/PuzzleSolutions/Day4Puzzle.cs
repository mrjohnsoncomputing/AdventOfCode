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

            var copies = new Dictionary<int, int>();
            for (var i = 0; i < scratchcards?.Count(); i++)
            {
                copies = AddCopiesToDictionary(copies, scratchcards[i], scratchcards);
            }

            var result = copies.Sum(kvp => kvp.Value);

            return $"{result}";
        }

        private Dictionary<int, int> AddCopiesToDictionary(Dictionary<int,int> copies, Scratchcard scratchcard, List<Scratchcard> scratchcards)
        {
            if (copies.ContainsKey(scratchcard.Id))
                copies[scratchcard.Id]++;
            else
                copies[scratchcard.Id] = 1;

            if (scratchcard.MatchingNumbers == 0)
                return copies;

            for (var j = scratchcard.Id; j < scratchcard.Id + scratchcard.MatchingNumbers; j++)
            {
                copies = AddCopiesToDictionary(copies, scratchcards[j], scratchcards);
            }

            return copies;
        }
    }
}
