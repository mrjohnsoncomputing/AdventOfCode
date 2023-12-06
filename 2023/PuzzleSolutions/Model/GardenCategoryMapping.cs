using PuzzleSolutions.Database.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Model;

public class GardenCategoryMapping
{
    public GardenCategoryMapping()
    {
        Mappings = new Dictionary<long, long>();
    }

    public Dictionary<long, long> Mappings { get; private set; }

    public void AddMapping(long sourceId, long destinationId, long count)
    {
        for (var i = 0; i < count; i++)
        {
            Mappings.Add(sourceId + i, destinationId + i);
        }
    }

    public long GetDestinationMapping(long source)
    {
        if (!Mappings.ContainsKey(source)) return source;

        return Mappings[source];
    }
}
