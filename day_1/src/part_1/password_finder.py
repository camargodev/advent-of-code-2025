class PasswordFinder:
    LEFT = 'L'
    MAX_VALUE = 99
    
    def find(self, lines):
        position = 50
        count_for_zeroes = 0
        for line in lines:
            side, total_num_clicks = line[0], int(line[1:])
            num_clicks = total_num_clicks % (self.MAX_VALUE + 1)
            if (side == self.LEFT):
                position -= num_clicks
                if (position < 0):
                    position = self.MAX_VALUE + position + 1
            else:
                position += num_clicks
                if (position > self.MAX_VALUE):
                    position = position - self.MAX_VALUE - 1
            if (position == 0):
                count_for_zeroes += 1
        return count_for_zeroes
