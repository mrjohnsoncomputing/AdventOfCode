using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.DataImporters
{
    //TODO: internal -> public
    public interface IDataImporter
    {
        public void Import();
    }
}
