class PaperRollFinder:
    PAPER_ROLL =  "@"


    def find(self, lines):
        _, adjacent_counts = self.count_paper_rolls_adjacent_in_line(lines)
        count_for_few_rolls = 0
        for i, symbol_line in enumerate(lines):
            totals_for_line = []
            for j, symbol in enumerate(symbol_line):
                counts_for_symbol = 0
                if symbol == self.PAPER_ROLL:
                    counts_for_symbol += adjacent_counts[i][j]-1
                    if i > 0:
                        counts_for_symbol += adjacent_counts[i-1][j]
                    if i < len(symbol_line)-1:
                        counts_for_symbol += adjacent_counts[i+1][j]
                    if counts_for_symbol < 4:
                        count_for_few_rolls += 1
                # print(i, j, symbol, counts_for_symbol)
                totals_for_line.append(counts_for_symbol)
            # print(totals_for_line)
        return count_for_few_rolls

    def count_paper_rolls_adjacent_in_line(self, lines):
        adjacent_counts = []
        symbol_map = []
        for line in lines:
            counts_for_line = []
            symbols_in_line = []
            count_for_first_pos = self.count_symbol(line[0]) + self.count_symbol(line[1])
            counts_for_line.append(count_for_first_pos)
            symbols_in_line.append(self.count_symbol(line[0]))

            for index in range(1, len(line)-1):
                count =  self.count_symbol(line[index-1]) + self.count_symbol(line[index]) + self.count_symbol(line[index+1])
                counts_for_line.append(count)
                symbols_in_line.append(self.count_symbol(line[index]))
                
            count_for_last_pos = self.count_symbol(line[-1]) + self.count_symbol(line[-2])
            counts_for_line.append(count_for_last_pos)
            symbols_in_line.append(self.count_symbol(line[-1]))

            adjacent_counts.append(counts_for_line)
            symbol_map.append(symbols_in_line)

        return (symbol_map, adjacent_counts)

    def count_symbol(self, symbol):
        return 1 if symbol == self.PAPER_ROLL else 0



