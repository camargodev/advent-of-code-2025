class MathMaker:
    def calculate(self, lines):
        lists_of_values, operations = self.extract_input(lines)
        total = 0
        for index, operation in enumerate(operations):
            value = 0 if operation == "+" else 1
            for list_of_values in lists_of_values:
                if operation == "+":
                    value += list_of_values[index]
                else:
                    value *= list_of_values[index]
            total += value
        return total

    def extract_input(self, lines):
        values = []
        operations = []
        for index, line in enumerate(lines):
            line_values = line.split()
            if index < len(lines) - 1:
                values.append([int(value) for value in line_values])
            else:
                operations = line_values
        return values, operations
