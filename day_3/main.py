from src.part_1.battery_finder import BatteryFinder as FirstBatteryFinder
from src.part_2.battery_finder import BatteryFinder as SecondBatteryFinder

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_3/res/input.txt", "r")]
    print(FirstBatteryFinder().find(lines))
    print(SecondBatteryFinder().find(lines))
