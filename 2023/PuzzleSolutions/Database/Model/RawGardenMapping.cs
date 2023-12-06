using PuzzleSolutions.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.Model
{
    public class RawGardenMapping : GenericDbModel
    {
        public RawGardenMapping() { }
        public RawGardenMapping(string sourceCategory, string destinationCategory, string source, string destination, string count) 
        {
            SourceCategory = Enum.Parse<GardeningCategory>(sourceCategory);
            DestinationCategory = Enum.Parse<GardeningCategory>(destinationCategory);
            Source = long.Parse(source);
            Destination = long.Parse(destination);
            Count = long.Parse(count);
        }

        public GardeningCategory SourceCategory { get; set; }
        public GardeningCategory DestinationCategory { get; set; }
        public long Source { get; set; }
        public long Destination { get; set; }
        public long Count { get; set; }
    }
}
