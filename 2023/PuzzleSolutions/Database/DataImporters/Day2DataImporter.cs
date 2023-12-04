using PuzzleSolutions.Database.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.DataImporters
{
    public class Day2DataImporter : DataImporterBase
    {
        public Day2DataImporter() : base(2) { }

        public void Import()
        {
            var dbContext = new Aoc2023DbContext();
            dbContext.Database.EnsureDeleted();
            dbContext.Database.EnsureCreated();

            var data = GetPuzzleDataFromFile();
            foreach (var line in data) 
            {
                var model = new CubeGame(line);
                dbContext.Day2?.Add(model);
            }
            dbContext.SaveChanges();
        }
    }
}
