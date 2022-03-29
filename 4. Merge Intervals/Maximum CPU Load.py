def max_load(jobs):
    jobs.sort(key=lambda x: x[0])

    s, e, l = 0, 1, 2

    end = jobs[0][e]
    load = jobs[0][l]
    maxLoad = -1

    for job in jobs[1:]:
        if job[s] < end:
            end = max(job[e], end)
            load += job[l]
        else:
            maxLoad = max(maxLoad, load)
            end = job[e]
            load = job[l]

    maxLoad = max(maxLoad, load)
    return maxLoad


jobs = [[1,4,3], [2,5,4], [7,9,6]]
print(max_load(jobs))

jobs = [[6,7,10], [2,4,11], [8,12,15]]
print(max_load(jobs))

jobs = [[1,4,2], [2,4,1], [3,6,5]]
print(max_load(jobs))
