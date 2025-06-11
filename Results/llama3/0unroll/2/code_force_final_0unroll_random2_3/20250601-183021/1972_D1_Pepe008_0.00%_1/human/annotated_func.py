#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, where 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
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
        
    #State: The output state is the sum of the number of pairs (i, j) for each test case, where i is a positive integer less than or equal to a, and j is a positive integer greater than or equal to 4 and less than or equal to b, such that (j+i) is divisible by the greatest common divisor of i and j. The sum is calculated for each test case and printed as the output.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains two positive integers 'a' and 'b'. For each test case, it calculates the sum of the number of pairs (i, j) where 'i' is a positive integer less than or equal to 'a' and 'j' is a positive integer greater than or equal to 4 and less than or equal to 'b', such that (j+i) is divisible by the greatest common divisor of 'i' and 'j'. The function then prints the calculated sum minus one for each test case.

