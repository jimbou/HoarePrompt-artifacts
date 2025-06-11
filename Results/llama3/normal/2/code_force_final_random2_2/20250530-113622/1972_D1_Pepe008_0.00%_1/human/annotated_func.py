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
        
    #State: T is greater than or equal to 0, t is T, a is an integer equal to the first integer from the input, b is an integer equal to the second integer from the input, info is a list of strings equal to the input, i is b + 1, x is ((a - b * (b - 1)) // b^2) + 1, suma is the sum of ((a - i * (i - 1)) // i^2) + 1 for all i from 1 to b where a - i * (i - 1) is greater than 0, and the value of suma - 1 is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains two positive integers n and m. For each test case, it calculates the sum of a specific formula for all integers i from 1 to m, and then prints the sum minus 1. The function does not modify the input values and does not have any side effects other than printing the calculated results.

