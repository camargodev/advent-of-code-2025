from src.part_1.fake_ids_finder import FakeIdsFinder as FirstFakeIdsFinder
from src.part_2.fake_ids_finder import FakeIdsFinder as SecondFakeIdsFinder

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_2/res/input.txt", "r")]
    print(FirstFakeIdsFinder().find(lines))
    print(SecondFakeIdsFinder().find(lines))
