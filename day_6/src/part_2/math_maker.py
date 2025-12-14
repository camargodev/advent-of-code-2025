import math

class MathMaker:
    BREAK = " "
    EMPTY = ""
    PLUS = "+"

    def calculate(self, lines):
        char_matrix, indexes = self.extract_break_indexes(lines)
        operations_sub_matrixes = self.extract_operations_sub_matrixes(char_matrix, indexes)
        num_of_operands, operations = self.extract_operations(lines)
        results = self.perform_operations(operations_sub_matrixes, operations, num_of_operands)
        return sum(results)
    
    def perform_operations(self, operations_sub_matrixes, operations, num_of_operands):
        results = []
        for index in range(len(operations_sub_matrixes)):
            sub_matrix = operations_sub_matrixes[index]
            operation = operations[index]
            values = self.extract_submatrix_values(sub_matrix, num_of_operands)
            result = self.perform_operation(values, operation)
            results.append(result)
        return results

    def perform_operation(self, values, operation):
        if operation == self.PLUS:
            return sum(values)
        return math.prod(values)

    def extract_submatrix_values(self, char_submatrix, num_of_operands):
        all_values = []
        lenght = len(char_submatrix[0])
        for index in range(lenght, 0, -1):
            column_index = index-1
            column_value = ""
            for line_index in range(num_of_operands):
                value = char_submatrix[line_index][column_index]
                if value == self.EMPTY:
                    continue
                column_value += value
            all_values.append(int(column_value))
        return all_values

    def extract_operations(self, lines):
        last_line = lines[-1]
        num_of_operands = len(lines)-1
        return num_of_operands, last_line.split()

    def extract_operations_sub_matrixes(self, char_matrix, indexes):
        operations_sub_matrixes = []
        start_index = 0
        end_index = indexes[0]
        for end_index in indexes:
            operations_sub_matrixes.append(self.extract_operation_matrix(char_matrix, start_index, end_index))
            start_index = end_index + 1
        operations_sub_matrixes.append(self.extract_operation_matrix(char_matrix, start_index, None))
        return operations_sub_matrixes

    def extract_operation_matrix(self, char_matrix, start, end_if_not_null):
        matrix = []
        for line in char_matrix:
            end = end_if_not_null if end_if_not_null is not None else len(line) 
            sub_line = line[start:end]
            matrix.append(sub_line)
        return matrix
    
    def extract_line_arrays(self, line):
        line_arrays = []
        last_was_break = False
        current_value_array = []
        for index, character in enumerate(line):
            if not last_was_break and character == self.BREAK and index > 0:
                last_was_break = True
                if len(current_value_array) > 0:
                    line_arrays.append(current_value_array)
                current_value_array = []
                continue
            
            value = int(character) if character != self.BREAK else None
            current_value_array.append(value)
            last_was_break = False
        if len(current_value_array) > 0:
            line_arrays.append(current_value_array)
        print(line_arrays)
        return line_arrays

    def extract_break_indexes(self, lines):
        char_matrix = []
        min_line_length = math.inf
        for index in range(0, len(lines)-1):
            char_matrix.append(list(lines[index]))
            min_line_length = min(min_line_length, len(lines[index]))

        break_indexes = []
        for vertical_index in range(0, min_line_length):
            if self.is_break_column(vertical_index, char_matrix):
                break_indexes.append(vertical_index)

        return char_matrix, break_indexes
    
    def is_break_column(self, index, char_matrix):
        for line_matrix in char_matrix:
            if line_matrix[index] != self.BREAK:
                return False
        return True
        
        
            

