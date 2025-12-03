import math

class PasswordFinder:
    LEFT = 'L'
    RIGHT = 'R'
    NUM_SLOTS = 100
    
    def find(self, lines):
        position = 50
        count_for_zeroes = 0
        for line in lines:
            side, total_num_clicks = line[0], int(line[1:])
            num_of_full_rotations = total_num_clicks // self.NUM_SLOTS
            remaining_number_of_clicks = total_num_clicks % self.NUM_SLOTS

            passed_through_zero = (side == self.LEFT and remaining_number_of_clicks >= position) or (side == self.RIGHT and (remaining_number_of_clicks + position) >= self.NUM_SLOTS)

            count_for_zeroes += num_of_full_rotations
            if (position != 0 and passed_through_zero):
                count_for_zeroes += 1

            if (side == self.LEFT):
                position -= remaining_number_of_clicks
            else:
                position += remaining_number_of_clicks

            if position < 0:
                position = self.NUM_SLOTS + position

            position = position % self.NUM_SLOTS

        return count_for_zeroes
