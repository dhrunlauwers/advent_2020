def find_seat(seat_string):
    """Finds a seat ID based on string provided on the boarding pass."""

    row = int(''.join([{'F':'0', 'B':'1'}[r] for r in seat_string[:7]]),2)
    col = int(''.join([{'L':'0', 'R':'1'}[c] for c in seat_string[7:]]),2)

    return row * 8 + col

def highest_seat_id(raw_seat_string):
    """Converts all seat strings into seat IDs
    and returns the highest seat ID found."""

    seat_list = raw_seat_string.split('\n')

    return max(list(map(find_seat, seat_list)))

class Plane:
    """Class to keep track of empty seats on a plane"""
    rows = list(range(0,128))
    cols = list(range(0,8))

    def __init__(self):
        """All seats start out empty"""
        self.empty_seats = [row * 8 + col for row in self.rows for col in self.cols]

    def seat_passenger(self, seat_id):
        """Each time a passenger is seated, the seat_id is removed from the empty seats list"""
        self.empty_seats.remove(seat_id)


# unit test
RAW = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""

assert highest_seat_id(RAW) == 820

#real problem
with open('./data/day05.txt') as f:
    inputs = f.read()

    print("Part 1:", highest_seat_id(inputs))

    plane = Plane()
    for seat in inputs.split('\n'):
        seat_id = find_seat(seat)
        plane.seat_passenger(seat_id)

    print("Part 2:", plane.empty_seats[48])