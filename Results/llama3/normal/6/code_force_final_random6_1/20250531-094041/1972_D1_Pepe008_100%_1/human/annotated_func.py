#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, such that 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
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
        
    #State: T is greater than or equal to 0, t is equal to T, a is a positive integer, b is a positive integer, stdin contains multiple test cases minus T test cases, i is equal to b, x is equal to (a - b * (b - 1)) // b^2 + 1, suma is increased by the sum of x values for all iterations where (a - i * (i - 1)) // i^2 + 1 > 0, and an additional 1 for iterations where (a - i * (i - 1)) % i^2 == 0 and i * (i - 1) % i^2 == 0, and the value of suma minus 2 is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains two positive integers n and m. It calculates a value based on these integers and prints the result minus 2 for each test case. The function processes all test cases and does not return any value.

