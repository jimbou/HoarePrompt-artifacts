#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two positive integers n, m (1 <= n, m <= 2 * 10^6).
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
        
    #State: T is an integer between 0 and 10^4 (inclusive), t is equal to T, stdin contains no test cases, info is a list containing two strings, a is a positive integer between 1 and 2 * 10^6 (inclusive), b is greater than or equal to 0, i is equal to b + 1, and suma is the sum of all x values calculated in each iteration of the loop, where x is ((a - i * (i - 1)) // i^2) + 1 if (a - i * (i - 1)) > 0, otherwise x is 0, and the value of suma - 1 is being printed, where suma - 1 is the sum of all x values calculated in each iteration of the loop minus 1

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains two positive integers n and m. It calculates the sum of a specific formula for each test case and prints the result minus one. The function does not modify the input values or store any results, it only prints the calculated values.

