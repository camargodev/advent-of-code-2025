class PaperRollFinder:
    PAPER_ROLL =  "@"
    EMPTY =  "."
    MAX_ADJACENT_ROLLS = 4

    def find(self, lines):
        has_rolls_to_remove = True
        total_rolls_to_remove = 0

        roll_matrix, adjacent_counts = self.count_paper_rolls_adjacent_in_line(lines)
        
        while has_rolls_to_remove:
            rolls_to_remove = []
            has_rolls_to_remove = False
            for i, roll_line in enumerate(roll_matrix):
                for j, roll in enumerate(roll_line):
                    counts_for_symbol = 0
                    if roll == self.PAPER_ROLL:
                        counts_for_symbol += adjacent_counts[i][j]-1
                        if i > 0:
                            counts_for_symbol += adjacent_counts[i-1][j]
                        if i < len(roll_line)-1:
                            counts_for_symbol += adjacent_counts[i+1][j]
                        
                        if counts_for_symbol < self.MAX_ADJACENT_ROLLS:
                            rolls_to_remove.append((i, j))
            
            if len(rolls_to_remove) > 0:
                has_rolls_to_remove = True
                total_rolls_to_remove += len(rolls_to_remove)
                roll_matrix, adjacent_counts = self.remove_rolls(roll_matrix, adjacent_counts, rolls_to_remove)

        return total_rolls_to_remove

    def count_paper_rolls_adjacent_in_line(self, lines):
        adjacent_counts = []
        roll_matrix = []
        for line in lines:
            counts_for_line = []
            rolls_in_line = []
            count_for_first_pos = self.count_symbol(line[0]) + self.count_symbol(line[1])
            counts_for_line.append(count_for_first_pos)
            rolls_in_line.append(line[0])

            for index in range(1, len(line)-1):
                count =  self.count_symbol(line[index-1]) + self.count_symbol(line[index]) + self.count_symbol(line[index+1])
                counts_for_line.append(count)
                rolls_in_line.append(line[index])
                
            count_for_last_pos = self.count_symbol(line[-1]) + self.count_symbol(line[-2])
            counts_for_line.append(count_for_last_pos)
            rolls_in_line.append(line[-1])

            adjacent_counts.append(counts_for_line)
            roll_matrix.append(rolls_in_line)

        return (roll_matrix, adjacent_counts)

    def remove_rolls(self, roll_matrix, adjacent_counts, rolls_to_remove):
        for (i, j) in rolls_to_remove:
            roll_matrix[i][j] = self.EMPTY
            adjacent_counts[i][j] = self.decrease_adjacent_if_needed(adjacent_counts[i][j])
            if j > 0:
                adjacent_counts[i][j-1] = self.decrease_adjacent_if_needed(adjacent_counts[i][j-1])
            if j < len( adjacent_counts[i]) - 1:
                adjacent_counts[i][j+1] = self.decrease_adjacent_if_needed(adjacent_counts[i][j+1])

        return  (roll_matrix, adjacent_counts)

    def count_symbol(self, symbol):
        return 1 if symbol == self.PAPER_ROLL else 0
    
    def decrease_adjacent_if_needed(self, value):
        return value-1 if value > 0 else value
