def tricky_sum(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return tricky_sum(n-1)
    else:
        return n + tricky_sum(n-2)
    
tricky_sum(5)