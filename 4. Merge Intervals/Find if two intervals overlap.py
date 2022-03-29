class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def check_overlap(intervals):
    intervals.sort(key=lambda x: x.start)

    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            return True
        else:
            end = interval.end

    return False


def main():
    print(check_overlap([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))
    print(check_overlap([Interval(1, 4), Interval(5, 6), Interval(7, 9)]))


main()
