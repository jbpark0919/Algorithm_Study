def func(n):
    
    if n == 0:
        return '-'
    else:
        return func(n-1) + ' '*pow(3, n-1) + func(n-1)

while(True):
    try:
        n = int(input())
        print(func(n))
    except:
        break
