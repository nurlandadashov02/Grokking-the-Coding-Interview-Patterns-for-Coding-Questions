appointments = [[4,5], [2,3], [3,6]]
appointments.sort(key= lambda x: x[0])

s, e = 0, 1

can_attend = True
for i in range(1, len(appointments)):
    if appointments[i][s] < appointments[i - 1][e]:
        can_attend = False
        break

print(can_attend)