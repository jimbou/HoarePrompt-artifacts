#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 * 10^6.
def func():
    T = int(input())
    for t in range(T):
        info = input().split()
        
        a, b = int(info[0]), int(info[1])
        
        suma = 0
        
        for i in range(1, b + 1):
            x = (a - i * (i - 1)) // i ** 2 + 1
            if (a - i * (i - 1)) // i ** 2 + 1 > 0:
                suma += x
                if (a - i * (i - 1)) % i ** 2 == 0 and i * (i - 1) % i ** 2 == 0:
                    suma += 1
        
        print(suma - 2)
        
    #State: For each of the T test cases, the output is the value of `suma - 2` after processing the corresponding `a` and `b` values.
#Overall this is what the function does:The function processes multiple test cases, each defined by two positive integers `a` and `b`. For each test case, it calculates a specific value based on these integers and outputs the result minus two.

