def calc(*numbers):
    countNumbers = len((numbers))
    result = 0;
    for i in range(countNumbers):
        result += numbers[i]

    return result / countNumbers

def main():
    print('Для числе 1, 2 и 3 среднее арифметическое будет:', calc(1, 2, 3))

if __name__ == '__main__':
    main()