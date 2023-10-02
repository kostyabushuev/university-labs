def fib(n):
    a = 1
    b = 1
    for i in range(n):
        result = a
        a, b = b, a + b
        yield result

with open('./static/Sam11_2_fibonaci.txt', 'a') as file:
    for value in fib(200):
        file.write(f'{value}\n')
        print(value)