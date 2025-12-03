class FakeIdsFinder:
    def find(self, lines):
        ranges = self.extract_ranges(lines)
        sum_of_invalid_ids = 0
        for (start, end) in ranges:
            for number in range(start, end + 1):
                if self.is_invalid(number):
                    sum_of_invalid_ids += number
        return sum_of_invalid_ids

    def extract_ranges(self, lines):
        pairs = []
        for line in lines:
            for part in line.split(","):
                a, b = part.split("-")
                pairs.append((int(a), int(b)))
        return pairs
    
    def is_invalid(self, number):
        string_number = str(number)
        # string + string contém s no meio se for repetição
        return string_number in (string_number + string_number)[1:-1]