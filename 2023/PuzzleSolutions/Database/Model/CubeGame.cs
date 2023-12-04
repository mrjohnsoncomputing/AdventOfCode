using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database.Model
{
    public class CubeGame : GenericDbModel
    {
        public CubeGame() { }
        
        public CubeGame(string gameData) 
        {
            var splitGameData = gameData.Split(": ")[1];
            var individualGames = splitGameData.Split("; ");
            foreach (var game in individualGames)
            {
                var games = game.Split(", ");
                foreach (var colours in games)
                {
                    var splitColour = colours.Split(" ");
                    var number = int.Parse(splitColour[0]);
                    var colour = splitColour[1];

                    switch (colour)
                    {
                        case "red":
                            if (number > Red) Red = number; 
                            break;
                        case "blue":
                            if (number > Blue) Blue = number;
                            break;
                        case "green":
                            if (number > Green) Green = number;
                            break;
                        default:
                            throw new Exception($"{colour} is not an expected colour.");
                    }
                }
            }
        }

        public int Red { get; private set; }
        public int Blue { get; private set; }
        public int Green { get; private set; }
    }
}
