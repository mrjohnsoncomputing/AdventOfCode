using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.Model
{
    public class CalibrationValue : GenericDbModel
    {
        public CalibrationValue() { }

        public CalibrationValue(string line) 
        {
            DigitsOnly = GetDigits(line);
            WithWords = GetDigitsAndWords(line);
        }
        public string DigitsOnly { get; private set; }
        public string WithWords { get; private set; }

        public string GetDigitsAndWords(string input)
        {
            var result = string.Empty;
            for (var i = 0; i < input.Length; i++)
            {
                var character = input[i];
                if (int.TryParse(character.ToString(), out var _))
                {
                    result += character;
                    continue;
                }

                if (i > input.Length - 3) continue;
                
                var size = 5;
                if (i > input.Length - 5) size = 4;
                if (i > input.Length - 4) size = 3;
                
                result += GetDigitFromWord(input.Substring(i, size));

            }
            return result;
        }

        private string GetDigitFromWord(string word)
        { 
            var mappings = new Dictionary<string, string>()
            {
                {"one", "1" },
                {"two", "2"},
                {"three", "3"},
                {"four", "4"},
                {"five", "5"},
                {"six", "6"},
                {"seven", "7"},
                {"eight", "8"},
                {"nine", "9"},
            };

            foreach (var mapping in mappings)
            {
                if (word.IndexOf(mapping.Key) == 0)
                {
                    return mapping.Value;
                }
            }
            return string.Empty;
        }

        public string GetDigits(string input)
        {
            var result = string.Empty;
            foreach (var character in input)
            {
                if (int.TryParse(character.ToString(), out var _))
                {
                    result += character;
                }
            }
            return result;
        }
    }
}
