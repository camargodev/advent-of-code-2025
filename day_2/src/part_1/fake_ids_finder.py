class FakeIdsFinder:
    def find(self, lines):
        ranges = self.extract_ranges(lines)
        sum_of_invalid_ids = 0
        for (start, end) in ranges:
            for number in range(start, end + 1):
                if self.has_two_equal_halves(number):
                    sum_of_invalid_ids += number
        return sum_of_invalid_ids

    def extract_ranges(self, lines):
        pairs = []
        for line in lines:
            for part in line.split(","):
                a, b = part.split("-")
                pairs.append((int(a), int(b)))
        return pairs
    
    def has_two_equal_halves(self, number):
        string_number = str(number)
        if len(string_number) % 2 != 0:
            return False
        mid = len(string_number) // 2
        return string_number[:mid] == string_number[mid:]