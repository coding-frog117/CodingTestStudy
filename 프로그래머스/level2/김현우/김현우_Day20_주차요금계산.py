from math import ceil


def calculate_time(time):
    h, m = map(int, time.split(":"))
    return 60 * h + m


def calculate_fee(time, a, b, c, d):
    if time <= a:
        return b
    else:
        return b + ceil((time - a) / c) * d


def solution(fees, records):
    answer = []
    d = {}

    for r in records:
        time, num, status = r.split()
        if status == "IN":
            if num in d.keys():
                d[num].append([calculate_time(time)])
            else:
                d[num] = [[calculate_time(time)]]
        else:
            d[num][-1].append(calculate_time(time))

    for k in d.keys():
        if len(d[k][-1]) == 1:
            d[k][-1].append(1439)

    for k in d.keys():
        temp = 0
        for s, e in d[k]:
            temp += e - s
        answer.append([k, calculate_fee(temp, *fees)])
    answer.sort()

    return [a[1] for a in answer]