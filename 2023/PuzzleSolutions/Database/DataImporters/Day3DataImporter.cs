using Microsoft.EntityFrameworkCore.Metadata.Internal;
using Microsoft.EntityFrameworkCore.Update.Internal;
using PuzzleSolutions.Database.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.DataImporters
{
    public class Day3DataImporter : DataImporterBase
    {
        public Day3DataImporter() : base(3) { }

        public void Import()
        {
            var data = GetPuzzleDataFromFile();
            ImportEngineParts(data);
            ImportGearRatios(data);
        }

        private void ImportGearRatios(string[] puzzleData)
        {
            using var dbContext = new Aoc2023DbContext();
            for (var row = 0; row < puzzleData.Length; row++)
            {
                for (var column = 0; column < puzzleData[row].Length; column++)
                {
                    var character = puzzleData[row][column];
                    if (character == '*')
                    {
                        if (IsValidGearRatio(puzzleData, row, column, out var gearRatio))
                        {
                            dbContext.GearRatios.Add(gearRatio!);
                        }
                    }
                }
            }
            dbContext.SaveChanges();
        }

        private bool IsValidGearRatio(string[] puzzleData, int row, int column, out GearRatio? gearRatio)
        {
            var foundNumbers = new List<int>();
            var rightHandNumber = FindNumber(puzzleData, row, column+1);
            if (rightHandNumber != null) foundNumbers.Add((int)rightHandNumber!);

            var leftHandNumber = FindNumber(puzzleData, row, column-1);
            if (leftHandNumber != null) foundNumbers.Add((int)leftHandNumber!);

            var topLeftNumber = FindNumber(puzzleData, row-1, column-1);
            var topRightNumber = FindNumber(puzzleData, row - 1, column + 1);
            var topMiddleNumber = FindNumber(puzzleData, row - 1, column);

            // 5.7
            if (topMiddleNumber == null)
            {
                // ..7
                if (topRightNumber != null) foundNumbers.Add((int)topRightNumber!);
                // 5..
                if (topLeftNumber != null) foundNumbers.Add((int)topLeftNumber!);
            }
            else
            {
                foundNumbers.Add((int)topMiddleNumber!);
            }

            var bottomLeftNumber = FindNumber(puzzleData, row + 1, column - 1);
            var bottomRightNumber = FindNumber(puzzleData, row + 1, column + 1);
            var bottomMiddleNumber = FindNumber(puzzleData, row + 1, column);

            // 5.7
            if (bottomMiddleNumber == null)
            {
                // ..7
                if (bottomRightNumber != null) foundNumbers.Add((int)bottomRightNumber!);
                // 5..
                if (bottomLeftNumber != null) foundNumbers.Add((int)bottomLeftNumber!);
            }
            else
            {
                foundNumbers.Add((int)bottomMiddleNumber!);
            }

            if (foundNumbers.Count == 2)
            {
                gearRatio = new GearRatio(foundNumbers[0], foundNumbers[1]);
                return true;
            }

            gearRatio = null;
            return false;
        }

        private int? FindNumber(string[] puzzleData, int row, int column)
        {
            var number = puzzleData[row][column].ToString();
            var rightHandSideIsNumeric = int.TryParse(number, out var _);
            if (!rightHandSideIsNumeric) return null;

            var isNumeric = true;
            var nextColumn = column - 1;
            while (isNumeric && nextColumn >= 0)
            {
                var nextNumber = puzzleData[row][nextColumn].ToString();
                isNumeric = int.TryParse(nextNumber, out var _);
                if (isNumeric)
                {
                    nextColumn--;
                    number = $"{nextNumber}{number}";
                }
            }

            isNumeric = true;
            nextColumn = column + 1;
            while (isNumeric && nextColumn < puzzleData[row].Length)
            {
                var nextNumber = puzzleData[row][nextColumn].ToString();
                isNumeric = int.TryParse(nextNumber, out var _);
                if (isNumeric)
                {
                    nextColumn++;
                    number = $"{number}{nextNumber}";
                }
            }

            return int.Parse(number);
        }

        private void ImportEngineParts(string[] puzzleData)
        {
            var dbContext = new Aoc2023DbContext();
            dbContext.Database.EnsureDeleted();
            dbContext.Database.EnsureCreated();

            var data = PadData(puzzleData);

            for (var row = 0; row < data.Length; row++)
            {
                var line = data[row];
                var number = string.Empty;
                for (var i = 0; i < line.Length; i++)
                {
                    var character = line[i];
                    var isNumeric = int.TryParse($"{number}{character}", out var _);
                    if (isNumeric)
                    {
                        number += character;
                    }
                    else
                    {
                        if (number.Length > 0)
                        {
                            var grid = new string[3];
                            var startPosition = i - number.Length;
                            var startOfLine = startPosition == 0;

                            startPosition -= startOfLine ? 0 : 1;

                            var paddingChar = string.Empty;
                            var linePadding = 2;
                            if (startOfLine)
                            {
                                paddingChar = ".";
                                linePadding = 1;
                            }


                            var lineSize = number.Length + linePadding;
                            grid[0] = row >= 1
                                ? paddingChar + data[row - 1].Substring(startPosition, lineSize)
                                : string.Empty;

                            grid[1] = paddingChar + line.Substring(startPosition, lineSize);

                            grid[2] = row < data.Length - 1
                                ? paddingChar + data[row + 1].Substring(startPosition, lineSize)
                                : string.Empty;

                            var model = new EnginePart(grid);
                            dbContext.Day3?.Add(model);

                            number = string.Empty;

                        }
                    }
                }
            }
            dbContext.SaveChanges();
        }

        public string[] PadData(string[] data)
        {
            var paddedData = data
                .ToList()
                .Select(line => line + ".")
                .ToArray();

            return paddedData;
        }
    }
}
