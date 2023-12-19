from functools import reduce

def distance(speed, t_time):
    d = speed * t_time
    return d


def solve(times, records):
    distances = []
    for k, race_time in enumerate(times):
        distances.append([])
        for i in range(race_time+1):
            speed = i
            t_time = race_time - i

            distances[k].append(distance(speed, t_time))

    for i, race in enumerate(distances):
        distances[i] = len(list(filter(lambda x: x > records[i], race)))


    return reduce(lambda x, y: x*y, distances)

times = [56, 97, 77, 93]
records = [499, 2210, 1097, 1440]
ans1 = solve(times, records)

times = [int(reduce(lambda x, y: str(x) + str(y), times))]
records = [int(reduce(lambda x, y: str(x) + str(y), records))]
ans2 = solve(times, records)

ans = (ans1, ans2)
print(ans)
