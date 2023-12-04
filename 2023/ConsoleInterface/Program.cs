// See https://aka.ms/new-console-template for more information
using PuzzleSolutions;
using PuzzleSolutions.Database.DataImporters;

Console.WriteLine("Hello, World!");

var importer = new Day3DataImporter();
Console.WriteLine("Importing...");
importer.Import();
Console.WriteLine("...Finished Importing");

var puzzleDay = new Day3Puzzle();
var part1Result = puzzleDay.SolvePart1();
Console.WriteLine($"Part 1: {part1Result}");

var part2Result = puzzleDay.SolvePart2();
Console.WriteLine($"Part 2: {part2Result}");

