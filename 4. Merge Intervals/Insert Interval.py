class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def insert(intervals, _interval):

    merged = []
    start = _interval.start
    end = _interval.end

    for i, interval in enumerate(intervals):
        if interval.end < start:
            merged.append(interval)
        elif interval.start <= end:
            end = max(interval.end, end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start, end))
    return merged


def main():
    print("Inserted intervals: ", end='')
    for i in insert([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6)):
        i.print_interval()
    print()

    print("Inserted intervals: ", end='')
    for i in insert([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10)):
        i.print_interval()
    print()

    print("Inserted intervals: ", end='')
    for i in insert([Interval(2, 3), Interval(5, 7)], Interval(1, 4)):
        i.print_interval()
    print()


main()