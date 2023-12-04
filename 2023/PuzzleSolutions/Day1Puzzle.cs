using PuzzleSolutions.Database;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions
{
    public class Day1Puzzle : IPuzzleDay
    {
        public string SolvePart1()
        {
            var dbContext = new Aoc2023DbContext();
            var result = dbContext.Day1?
                .ToList()
                .Select(num => int.Parse($"{num.DigitsOnly[0]}{num.DigitsOnly[num.DigitsOnly.Length - 1]}"))
                .Sum();

            return $"{result}";
        }

        public string SolvePart2()
        {
            var dbContext = new Aoc2023DbContext();
            var result = dbContext.Day1?
                .ToList()
                .Select(num => int.Parse($"{num.WithWords[0]}{num.WithWords[num.WithWords.Length - 1]}"))
                .Sum();

            return $"{result}";
        }
    }
}
