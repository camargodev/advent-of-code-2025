from src.part_1.password_finder import PasswordFinder as FirstPasswordFinder
from src.part_2.password_finder import PasswordFinder as SecondPasswordFinder

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_1/res/input.txt", "r")]
    print(FirstPasswordFinder().find(lines))
    print(SecondPasswordFinder().find(lines))
