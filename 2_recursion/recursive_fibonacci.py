# Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]
# Each number: fm = fm-1 + fm-2
def fibonacci(n):
    #print("now n=",n)
    if n <= 1:
        return n
    else:
        #print("call fibonacci with n-1=",n - 1)
        fm1 = fibonacci(n - 1)
        #print("call fibonacci with n-2=",n - 2)
        fm2 = fibonacci(n - 2)
        fm = fm1 + fm2
        #print("resulting ",fm2,"+",fm1,"->",fm)
        return fm 

n = 4 # index of fibonacci number, starting from 0
print(fibonacci(n))
