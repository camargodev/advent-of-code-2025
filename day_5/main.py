from src.part_1.ingredient_checker import IngredientChecker as FirstIngredientChecker
from src.part_2.ingredient_checker import IngredientChecker as SecondIngredientChecker

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_5/res/input.txt", "r")]
    print(FirstIngredientChecker().check(lines))
    print(SecondIngredientChecker().check(lines))
