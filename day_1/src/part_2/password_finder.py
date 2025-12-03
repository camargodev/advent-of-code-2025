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
            print(position, side, total_num_clicks)
            # num_of_full_rotations = total_num_clicks // self.NUM_SLOTS

            passed_through_zero = (side == self.LEFT and total_num_clicks >= position) or (side == self.RIGHT and (total_num_clicks + position) >= self.NUM_SLOTS)

            # count_for_zeroes += num_of_full_rotations
            if (position != 0 and passed_through_zero):
                print("+1")
                count_for_zeroes += 1

            if (side == self.LEFT):
                position -= total_num_clicks
            else:
                position += total_num_clicks

            if position < 0:
                position = self.NUM_SLOTS + position

            position = position % self.NUM_SLOTS
            print()

        return count_for_zeroes
