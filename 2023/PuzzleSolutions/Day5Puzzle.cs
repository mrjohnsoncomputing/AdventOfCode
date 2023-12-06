using PuzzleSolutions.Database;
using PuzzleSolutions.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions
{
    internal class Day5Puzzle : IPuzzleDay
    {
        public string SolvePart1()
        {
            using var dbContext = new Aoc2023DbContext();

            var seeds = dbContext.Seeds?.ToList();

            var mappingData = dbContext.Day5?.ToList();

            var locations = new List<long>();
            foreach (var seed in seeds!)
            {
                var destination = GardeningCategory.soil;
                var counter = 1;
                var sourceId = seed.Identifier;
                while (counter <= (int)GardeningCategory.location)
                {
                    var existingMapping = mappingData!
                        .Where(model => model.DestinationCategory == destination)
                        .Where(model => sourceId >= model.Source && sourceId < model.Source + model.Count)
                        .ToList();
                    
                    if (existingMapping.Any()) 
                    {
                        var mapping = existingMapping[0];
                        var difference = sourceId - mapping.Source;
                        sourceId = mapping.Destination + difference;
                    }
                   
                    counter++;
                    destination = (GardeningCategory)counter;
                }

                locations.Add(sourceId);
            }

            return $"{locations.Min()}";
        }

        public string SolvePart2()
        {
            using var dbContext = new Aoc2023DbContext();

            var rawSeeds = dbContext.Seeds?.ToList();

            var seeds = new List<long>();
            for (var i = 0; i < rawSeeds!.Count; i += 2)
            {
                Console.WriteLine($"Seed: {i}");
                for (var j = rawSeeds[i].Identifier; j < rawSeeds[i].Identifier + rawSeeds[i +1].Identifier; j++)
                {
                    seeds.Add(j);
                }
            }


            var mappingData = dbContext.Day5?.ToList();

            var locations = new List<long>();
            Console.WriteLine($"Total Seeds: {seeds.Count()}");
            foreach (var seed in seeds!)
            {
                var destination = GardeningCategory.soil;
                var counter = 1;
                var sourceId = seed;
                while (counter <= (int)GardeningCategory.location)
                {
                    var existingMapping = mappingData!
                        .Where(model => model.DestinationCategory == destination)
                        .Where(model => sourceId >= model.Source && sourceId < model.Source + model.Count)
                        .ToList();

                    if (existingMapping.Any())
                    {
                        var mapping = existingMapping[0];
                        var difference = sourceId - mapping.Source;
                        sourceId = mapping.Destination + difference;
                    }

                    counter++;
                    destination = (GardeningCategory)counter;
                }

                locations.Add(sourceId);
            }

            return $"{locations.Min()}";
        }
    }
}
