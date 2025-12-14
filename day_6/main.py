from src.part_1.math_maker import MathMaker as FirstMathMaker
from src.part_2.math_maker import MathMaker as SecondMathMaker

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_6/res/input.txt", "r")]
    print(FirstMathMaker().calculate(lines))
    print(SecondMathMaker().calculate(lines))
