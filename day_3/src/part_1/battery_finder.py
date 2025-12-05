class BatteryFinder:
    def find(self, lines):
        total = 0
        for line in lines:
            first_ocurrence = dict()
            last_ocurrence = dict()
            for index, value in enumerate(line):
                number = int(value)
                if number not in first_ocurrence:
                    first_ocurrence[number] = index
                last_ocurrence[number] = index

            
            last_index = len(line) - 1
        
            highest_first_digit = self.find_highest_in_map(first_ocurrence, min_index=-1, max_index=last_index-1)
            highest_first_index = first_ocurrence[highest_first_digit]

            highest_second_digit = self.find_highest_in_map(last_ocurrence, min_index=highest_first_index, max_index=last_index)

            highest_value_on_line = highest_first_digit*10 + highest_second_digit
            total += highest_value_on_line
        return total


    def find_highest_in_map(self, map, min_index, max_index):
        highest_expected = 9
        found = False
        while (highest_expected > -1 and not found):
            if highest_expected in map and map[highest_expected] > min_index and map[highest_expected] <= max_index:
                found = True
            else:
                highest_expected -= 1
        return highest_expected
