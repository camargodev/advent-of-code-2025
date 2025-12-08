class IngredientChecker:
    def check(self, lines):
        ranges = self.extract_input(lines)
        sorted_ranges =  sorted(ranges, key=lambda x: x[0])
        merged_ranges = []

        for start, end in sorted_ranges:
            if not merged_ranges or start > merged_ranges[-1][1]:
                merged_ranges.append([start, end])
            else:
                merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

        merged_length = 0
        for merged_range in merged_ranges:
            merged_length += merged_range[1]-merged_range[0]+1
        return merged_length
    
    def extract_input(self, lines):
        index = 0
        ranges = []
        while len(lines[index]) > 0:
            start, end = lines[index].split("-")
            ranges.append((int(start), int(end)))
            index += 1

        return ranges