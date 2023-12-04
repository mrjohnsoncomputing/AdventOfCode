using PuzzleSolutions.Database;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions
{
    public class Day2Puzzle : IPuzzleDay
    {
        public string SolvePart1()
        {
            var dbContext = new Aoc2023DbContext();
            var result = dbContext.Day2?
                .ToList()
                .Where(model => model.Red <= 12 && model.Green <= 13 && model.Blue <= 14)
                .Select(model => model.Id)
                .Sum();

            return $"{result}";
        }

        public string SolvePart2()
        {
            var dbContext = new Aoc2023DbContext();
            var result = dbContext.Day2?
                .ToList()
                .Select(model => model.Red * model.Blue * model.Green)
                .Sum();

            return $"{result}";
        }
    }
}
