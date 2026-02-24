def caching_fibonacci():
    """
    Повертає функцію fibonacci(n) з кешуванням.
    Використовує замикання для збереження стану cache між викликами.
    """
    cache = {} # cache зберігає вже обчислені значення Fibonacci

    # функція fibonacci(n) повертає число
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: 
            return cache[n] # якщо значення вже обчислено — повертаємо з кешу
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci
    
# Отримуємо функцію fibonacci. Кожен виклик `caching_fibonacci()` створює свій окремий cache
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))


