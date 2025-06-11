#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a positive integer t (1 <= t <= 10^4), representing the number of test cases. Each of the following lines contains two positive integers n and m (1 <= n, m <= 2 * 10^6), representing the input for each test case.
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
        
    #State: T is a positive integer between 1 and 10^4 (inclusive), t is equal to T, stdin contains no lines of input, a is a positive integer, b is a positive integer, i is equal to b + 1, x is ((a - b * (b - 1)) // b^2) + 1, suma is the sum of ((a - i * (i - 1)) // i^2) + 1 for i from 1 to b. If ((a - i * (i - 1)) % i^2 == 0 and i * (i - 1) % i^2 == 0) for some i, then suma is incremented by the number of times this condition is true, and the value of suma - 2 is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two positive integers, n and m. It then calculates a sum based on a specific formula involving n and m, and prints the result minus 2 for each test case. The function processes all test cases and does not return any value.

