using Microsoft.EntityFrameworkCore;
using PuzzleSolutions.Database.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PuzzleSolutions.Database
{
    public class Aoc2023DbContext : DbContext
    {
        public DbSet<CalibrationValue>? Day1 { get; set; }
        public DbSet<CubeGame>? Day2 { get; set; }
        public DbSet<EnginePart>? Day3 { get; set; }
        public DbSet<GearRatio> GearRatios { get; set; }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(
                "Server=127.0.0.1,1433;Database=Aoc2023;User Id=sa;Password='Password1';Encrypt=False");
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            ConfigureId<CalibrationValue>(modelBuilder);
            ConfigureId<CubeGame>(modelBuilder);
            ConfigureId<EnginePart>(modelBuilder);
            ConfigureId<GearRatio>(modelBuilder);
        }

        private void ConfigureId<T>(ModelBuilder modelBuilder) where T : GenericDbModel
        {
            modelBuilder.Entity<T>()
                .HasKey(model => model.Id)
                .HasName($"{typeof(T).ToString().Split(".").Last()}_Id");
        }
    }
}
