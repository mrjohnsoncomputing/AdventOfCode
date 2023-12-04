using PuzzleSolutions.Database;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions
{
    public class Day3Puzzle : IPuzzleDay
    {
        public string SolvePart1()
        {
            using var dbContext = new Aoc2023DbContext();
            var result = dbContext.Day3?
                .ToList()
                .Where(model => model.IsValid)
                .Sum(model => model.Number);

            return $"{result}";
        }

        public string SolvePart2()
        {
            using var dbContext = new Aoc2023DbContext();
            var result = dbContext.GearRatios?
                .ToList()
                .Sum(model => model.Ratio);

            return $"{result}";
        }
    }
}
