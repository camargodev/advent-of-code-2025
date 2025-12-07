class IngredientChecker:
    def check(self, lines):
        ranges, values = self.extract_input(lines)
        
        fresh_ingredient_count = 0
        for ingredient_value in values:
            if self.check_if_fresh(ingredient_value, ranges):
                fresh_ingredient_count += 1

        return fresh_ingredient_count
    
    def check_if_fresh(self, value, ranges):
        for (start, end) in ranges:
            if start <= value and end >= value:
                return True
        return False

    def extract_input(self, lines):
        index = 0
        ranges = []
        while len(lines[index]) > 0:
            start, end = lines[index].split("-")
            ranges.append((int(start), int(end)))
            index += 1
        
        index += 1
        values = []
        while index < len(lines):
            values.append(int(lines[index]))
            index += 1

        return ranges, values