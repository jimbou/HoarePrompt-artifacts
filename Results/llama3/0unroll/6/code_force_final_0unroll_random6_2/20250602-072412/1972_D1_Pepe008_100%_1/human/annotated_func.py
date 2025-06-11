#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
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
        
    #State: The output state will be the sum of the number of positive integers less than or equal to b, minus 2, for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains two positive integers n and m. For each test case, it calculates the sum of the number of positive integers less than or equal to m, minus 2, and prints the result. The function processes all test cases and outputs the calculated sums.

