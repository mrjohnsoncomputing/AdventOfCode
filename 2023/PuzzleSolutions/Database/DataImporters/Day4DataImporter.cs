using Microsoft.EntityFrameworkCore.Metadata.Internal;
using Microsoft.EntityFrameworkCore.Update.Internal;
using PuzzleSolutions.Database.Model;
using PuzzleSolutions.Extensions;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.DataImporters
{
    internal class Day4DataImporter : DataImporterBase, IDataImporter
    {
        public Day4DataImporter() : base(4) { }

        public void Import()
        {
            var data = GetPuzzleDataFromFile();
            var scratchcardNumbers = data
                .ToList()
                .Select(line => line.Split(": ")[1].Split(" | "))
                .ToArray();

            using var dbContext = new Aoc2023DbContext();
            dbContext.Database.EnsureDeleted();
            dbContext.Database.EnsureCreated();
            foreach (var numberType in scratchcardNumbers)
            {
                var scratchcard = new Scratchcard(numberType[0].Replace("  ", " ").Trim(), numberType[1].Replace("  ", " ").Trim());
                dbContext.Day4?.Add(scratchcard);
            }
            dbContext.SaveChanges();
        }
    }
}
