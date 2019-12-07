#Fibonacci series:
#the sum of two elements defined the next
# 1 1 2 3 5 8 
def fib(n):
    a=0
    b=1
    while a < n:
        print(a)
        a, b = b, a+b