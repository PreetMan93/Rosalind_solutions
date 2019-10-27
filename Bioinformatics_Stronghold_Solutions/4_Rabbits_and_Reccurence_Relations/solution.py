#When N = 5 and K = 3:
#Month 1 = 1 , Month 2 = 1 , Month 3 = 4, Month 4 = 7, Month 5 = 19
#Therefore, F(n) = F(N-1) + F(n-2) * K where F(2) = F(1) = 1

#Using memoization to stop overlapping computations:
def fib(N,K,Cache):
    if N == 0 or N == 1 or N == 2:
        Cache[N] = 1
    elif not N in Cache:
        Cache[N] = fib(N-1,K,Cache) + fib(N-2,K,Cache) * K
    return Cache[N]

print(fib(5,3,{}))

