value = input('Введите предложение: ')

print('Длина предложения:', len(value))
print('Предложение в нижнем регистре:', value.lower())

words = 0
for i in range(len(value)):
    if value[i] in ['a', 'e', 'i', 'o', 'u']:
        words += 1
print('Количество гласных в предложении:', words)

print('Замена "ugly" на "beauty":', value.replace('ugly', 'beauty'))
print('Предложение начинается на The:', 'да' if value.find('The') == 0 else 'нет')
print('Предложение заканчивается на end:', 'да' if value.find('end') == len(value) - len('end') else 'нет')
