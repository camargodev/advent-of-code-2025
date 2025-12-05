class BatteryFinder:
    NUM_DIGITS = 12

    def find(self, lines):
        total = 0
        for line in lines:
            ocurrences = dict()
            for index, value in enumerate(line):
                number = int(value)
                if number not in ocurrences:
                    ocurrences[number] = []
                ocurrences[number].append(index)

            highest_in_line = self.find_highest_in_line(len(line), ocurrences)
            total += highest_in_line
        return total
    

    def find_highest_in_line(self, total_num_of_digits, map):
        position = self.NUM_DIGITS
        highest_ordered_list = []
        min_index = -1
        while (position > 0):
            max_index = total_num_of_digits - position
            (highest_value, min_index) = self.find_highest_in_map(map, max_index, min_index)
            highest_ordered_list.append(highest_value)
            position -= 1

        total = 0
        for (index, number) in enumerate(highest_ordered_list):
            multiplier = self.NUM_DIGITS - index - 1
            multiplied_number = number * (10 ** multiplier)
            total += multiplied_number

        return total

    def find_highest_in_map(self, map, max_index, min_index):
        highest_expected = 9
        while (highest_expected > -1):
            if highest_expected in map:
                ocurrences_for_number = map[highest_expected]
                for index in ocurrences_for_number:
                    if index > min_index and index <= max_index:
                        return (highest_expected, index)
            highest_expected -= 1
        return (None, None)
