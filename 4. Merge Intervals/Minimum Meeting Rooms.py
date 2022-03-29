def num_rooms(meetings):
    meetings.sort(key= lambda x: x[0])

    start, end = 0, 1

    rooms = [meetings[0]]

    for i in range(1, len(meetings)):
        found = False
        for meet in rooms:
            if meetings[i][start] >= meet[end]:
                found = True
                break

        if not found:
            rooms.append(meetings[i])

    return len(rooms)

meetings = [[1,4], [2,5], [7,9]]
print(num_rooms(meetings))

meetings = [[6,7], [2,4], [8,12]]
print(num_rooms(meetings))

meetings = [[1,4], [2,3], [3,6]]
print(num_rooms(meetings))

meetings = [[4,5], [2,3], [2,4], [3,5]]
print(num_rooms(meetings))