#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, where 1 <= n, m <= 2 * 10^6.
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
        
    #State: T is greater than or equal to 0, t is equal to T, a is an integer equal to the first integer in the input, b is an integer equal to the second integer in the input, stdin is empty, suma is equal to the sum of x values calculated in each iteration of the loop, and the value of suma minus 2 is being printed, i is equal to b, and the value of suma minus 2 is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains two positive integers n and m. For each test case, it calculates a sum of values based on a formula involving n and m, and then prints the calculated sum minus 2. The function processes all test cases and empties the standard input.

