// See https://aka.ms/new-console-template for more information
using PuzzleSolutions;
using PuzzleSolutions.Database;
using PuzzleSolutions.Database.DataImporters;

Console.WriteLine("Hello, World!");

var day = 4;
DataImportManager.ImportAll(day);
PuzzleManager.SolveAll(day);