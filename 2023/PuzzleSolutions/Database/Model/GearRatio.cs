using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.Model
{
    public class GearRatio : GenericDbModel
    {
        public GearRatio() { }

        public GearRatio(int part1, int part2) 
        {
            Part1 = part1;
            Part2 = part2;
            Ratio = Part1 * Part2;
        }

        public int Part1 { get; private set; }
        public int Part2 { get; private set; }
        public int Ratio { get; private set; }
    }
}
