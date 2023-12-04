using PuzzleSolutions.Database.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.DataImporters
{
    public class Day1DataImporter : DataImporterBase
    {
        public Day1DataImporter() : base(1) { }

        public void Import()
        {
            var dbContext = new Aoc2023DbContext();
            dbContext.Database.EnsureDeleted();
            dbContext.Database.EnsureCreated();

            var data = GetPuzzleDataFromFile();
            foreach (var line in data) 
            {
                var model = new CalibrationValue(line);
                dbContext.Day1?.Add(model);
            }
            dbContext.SaveChanges();
        }
    }
}
