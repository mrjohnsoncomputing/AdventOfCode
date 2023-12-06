using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.Model
{
    public class Seed : GenericDbModel
    {
        public Seed() { }
        public Seed(long id) 
        {
            Identifier = id;
        }

        public Seed(string id)
        {
            Identifier = long.Parse(id);
        }

        public long Identifier { get; set; }
    }
}
