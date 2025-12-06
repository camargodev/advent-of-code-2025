from src.part_1.paper_roll_finder import PaperRollFinder as FirstPaperRollFinder
from src.part_2.paper_roll_finder import PaperRollFinder as SecondPaperRollFinder

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_4/res/input.txt", "r")]
    print(FirstPaperRollFinder().find(lines))
    print(SecondPaperRollFinder().find(lines))
