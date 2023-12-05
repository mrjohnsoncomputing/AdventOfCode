using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Extensions
{
    static public class IEnumerableExtensions
    {
        public static int[] ConvertToIntArray(this IEnumerable<string> array)
        {
            var result = new List<int>();
            foreach (var item in array)
            {
                var intItem = int.Parse(item);
                result.Add(intItem);
            }
            return result.ToArray(); ;
        }

        public static void Print<T>(this IEnumerable<T> list)
        {
            foreach (var item in list)
            {
                Console.Write($"{item} ");
            }
        }

        public static string Stringify<T>(this IEnumerable<T> list)
        {
            var result = string.Empty;
            foreach (var item in list)
            {
                result += $"{item} ";
            }
            return result.Trim();
        }
    }
}
