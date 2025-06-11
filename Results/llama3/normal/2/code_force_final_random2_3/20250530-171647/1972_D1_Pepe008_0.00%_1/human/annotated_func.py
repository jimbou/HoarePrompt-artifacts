#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, such that 1 <= n, m <= 2 * 10^6.
    T = int(input())
    for t in range(T):
        info = input().split()
        
        a, b = int(info[0]), int(info[1])
        
        """for i in range(1,a+1):
                for j in range(4,b+1):
                    if int((j+i)%(j*math.gcd(i,j))) == 0:
                        print(i,j)"""
        
        suma = 0
        
        for i in range(1, b + 1):
            x = (a - i * (i - 1)) // i ** 2 + 1
            if a - i * (i - 1) > 0:
                suma += x
        
        print(suma - 1)
        
    #State: T is a positive integer, t is equal to T, stdin contains no test cases, info is a list of two strings, a is a positive integer between 1 and 2 * 10^6, b is a positive integer between 1 and 2 * 10^6, i is equal to b, suma is a positive integer between 0 and 2 * 10^6, and the value of suma - 1 is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. For each test case, it calculates the number of pairs (i, j) that satisfy a specific condition and prints the result minus one. The function processes all test cases and prints the results accordingly.

