class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def intersect(intervals1, intervals2):

    intersection = []

    for interval1 in intervals1:
        for interval2 in intervals2:
            if interval1.start <= interval2.end and interval1.end >= interval2.start:
                start = max(interval1.start, interval2.start)
                end = min(interval1.end, interval2.end)
                intersection.append(Interval(start, end))
            elif interval1.end < interval2.start:
                break
            else:
                continue


    return intersection


def main():
    print("Intersect intervals: ", end='')
    for i in intersect([Interval(1, 3), Interval(5, 6), Interval(7, 9)], [Interval(2, 3), Interval(5, 7)]):
        i.print_interval()
    print()

    print("Intersect intervals: ", end='')
    for i in intersect([Interval(1, 3), Interval(5, 7), Interval(9, 12)], [Interval(5, 10)]):
        i.print_interval()
    print()


main()
