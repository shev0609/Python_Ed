### Задача № 9.
### По данному целому неотрицательному n вычислите значение n!.
### N! = 1*2*3*...*N (произведение всех числел от 1 до N) 0! = 1.
### Решить задачу используя цикл while.
### Input: 5. Output: 120.

### Решение
n = int(input('Введите число: '))
a = 1 
result = 1
while a <= n:
    result = result * a
### result *= a * Можно сократить строку вот так
    a += 1
### a = a + 1 * На место (a += 1)
print(result)