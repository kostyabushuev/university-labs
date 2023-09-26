receipts = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666, 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928, 5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]

print('Выдано чеков:', len(receipts))

unique_recepts = [];
for x in receipts:
    if x not in unique_recepts:
        unique_recepts.append(x)
print('Количество разных людей посетивших ресторан:', len(unique_recepts))

biggest_count_visit = tuple([-1, 0])
for x in receipts:
    savedCode, savedCount = biggest_count_visit
    count = receipts.count(x)
    if count > savedCount:
        biggest_count_visit = tuple([x, count])
print('Больше всех посетил работник:', biggest_count_visit[0])


