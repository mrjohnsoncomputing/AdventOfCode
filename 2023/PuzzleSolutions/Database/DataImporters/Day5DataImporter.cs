using PuzzleSolutions.Database.Model;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.DataImporters
{
    internal class Day5DataImporter : DataImporterBase, IDataImporter
    {
        public Day5DataImporter() : base(5) { }

        public void Import()
        {
            var data = GetPuzzleDataFromFile();

            var seeds = data[0]
                .Replace("seeds: ", string.Empty)
                .Split(" ");

            using var dbContext = new Aoc2023DbContext();
            foreach (var seedId in seeds)
            {
                dbContext.Seeds?.Add(new Seed(seedId));
            }

            dbContext.SaveChanges();

            var sourceCategory = string.Empty;
            var destinationCategory = string.Empty;
            foreach (var line in data.ToList().GetRange(1, data.Length - 1))
            {
                if (line == string.Empty) continue;

                if (line.Contains("-to-"))
                {
                    var mapping = line
                        .Split(' ')[0]
                        .Split("-to-");

                    sourceCategory = mapping[0];
                    destinationCategory = mapping[1];
                    continue;
                }

                var ids = line.Split(' ');
                var sourceId = ids[1];
                var destinationId = ids[0];
                var count = ids[2];

                dbContext.Day5?.Add(new RawGardenMapping(
                    sourceCategory,destinationCategory,sourceId,destinationId,count));
            }
            dbContext.SaveChanges();

        }
    }
}
