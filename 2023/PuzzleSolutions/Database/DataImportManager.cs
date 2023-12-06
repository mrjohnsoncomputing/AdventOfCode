using PuzzleSolutions.Helpers;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database
{
    static public class DataImportManager
    {
        public static void ImportSingleDay(int day)
        {
            ResetDb();
            Import(day);
        }

        public static void ImportAll(int limit)
        {
            ResetDb();
            for (var i = 0; i < limit; i++)
            {
                Import(i + 1);
            }
        }

        private static void Import(int day)
        {
            var importer = Instantiator.InstantiateImporter(day);
            Console.WriteLine("Importing...");
            importer.Import();
            Console.WriteLine("...Finished Importing");
        }

        private static void ResetDb()
        {
            using var dbContext = new Aoc2023DbContext();
            dbContext.Database.EnsureDeleted();
            dbContext.Database.EnsureCreated();
        }

        
    }
}
