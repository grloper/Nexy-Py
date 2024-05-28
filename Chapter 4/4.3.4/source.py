def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        

fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))