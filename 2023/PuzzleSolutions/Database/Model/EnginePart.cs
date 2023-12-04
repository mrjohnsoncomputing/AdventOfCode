using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.Model
{
    public class EnginePart : GenericDbModel
    {
        public EnginePart() { }

        public EnginePart(string[] grid)
        {
            Console.WriteLine($"Length: {grid[1].Length} | {grid[1]}");
            Number = int.Parse(grid[1].Substring(1, grid[1].Length - 2));
            IsValid = false;

            foreach (var line in grid)
            {
                foreach (var character in line)
                {
                    if (int.TryParse(character.ToString(), out var _) || character == '.') continue;

                    IsValid = true;

                }
            }
        }
        public int Number { get; private set; }
        public bool IsValid { get; private set; }
    }
}
