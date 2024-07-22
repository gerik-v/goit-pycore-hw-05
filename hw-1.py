def caching_fibonacci():
    # dictionary for cache
    cache = {}

    def fibonacci(n):
        if n == 1:
            return 1
        elif n <= 0:
            return 0
     
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

try:
    n = int(input("Введіть номер числа Фібоначчі: "))
    print(f"Число Фібоначчі для n={n}: {fib(n)}")
except ValueError:
    print("Будь ласка, введіть ціле число.")

