using PuzzleSolutions.Database.DataImporters;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Helpers
{
    public class Instantiator
    {
        public static IPuzzleDay InstantiatePuzzleDay(int day)
        {
            var instance = GetInstance($"PuzzleSolutions.Day{day}Puzzle");
            if (instance == null) throw new Exception($"Unable to create Puzzle instance for day {day}");
            return (IPuzzleDay)instance;
        }

        public static IDataImporter InstantiateImporter(int day)
        {
            var instance = GetInstance($"PuzzleSolutions.Database.DataImporters.Day{day}DataImporter");
            if (instance == null) throw new Exception($"Unable to create Importer instance for day {day}");
            return (IDataImporter)instance;
        }

        private static object? GetInstance(string fullyQualifiedName)
        {
            var type = Type.GetType(fullyQualifiedName);
            if (type != null)
                return Activator.CreateInstance(type);
            foreach (var assembly in AppDomain.CurrentDomain.GetAssemblies())
            {
                type = assembly.GetType(fullyQualifiedName);
                if (type != null)
                    return Activator.CreateInstance(type);
            }
            return null;
        }
    }
}
