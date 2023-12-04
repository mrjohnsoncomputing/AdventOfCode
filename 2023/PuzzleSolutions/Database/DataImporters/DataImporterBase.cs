using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.DataImporters
{
    public class DataImporterBase
    {
        private int _day;
        private int _part;

        protected DataImporterBase(int day, int part=1)
        {
            _day = day;
            _part = part;
        }

        protected string[] GetPuzzleDataFromFile()
        {
            var dataFilePath = Path
                .Combine(Environment.CurrentDirectory, $"Data-Work/Day{_day}-{_part}.txt");
            var data = File.ReadAllLines( dataFilePath );
            return data;
        }
    }
}
