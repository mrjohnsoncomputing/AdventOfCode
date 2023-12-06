using PuzzleSolutions.Helpers;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions
{
    static public class PuzzleManager
    {
        public static void SolveSingleDay(int day)
        {
            Solve(day);
        }

        public static void SolveAll(int limit)
        {
            for (var i = 0; i < limit; i++)
            {
                Solve(i + 1);
            }
        }

        private static void Solve(int day)
        {
            var puzzle = Instantiator.InstantiatePuzzleDay(day);
            Console.WriteLine($"#### Day {day} Results ####");
            var part1Result = puzzle.SolvePart1();
            Console.WriteLine($"Part 1: {part1Result}");

            var part2Result = puzzle.SolvePart2();
            Console.WriteLine($"Part 2: {part2Result}\n");
        }
    }
}
