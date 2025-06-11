#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, where 1 <= n, m <= 2 * 10^6.
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
        
    #State: The number of pairs (i, j) such that 1 <= i <= a, 4 <= j <= b, and (j + i) is divisible by j times the greatest common divisor of i and j, minus 1, for each test case.

#Overall this is what the function does:This function calculates and prints the number of pairs (i, j) such that 1 <= i <= a, 4 <= j <= b, and (j + i) is divisible by j times the greatest common divisor of i and j, minus 1, for each test case provided in the input. It takes no arguments and returns no value, instead printing the result for each test case.

