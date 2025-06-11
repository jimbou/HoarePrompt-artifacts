#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a positive integer t (1 <= t <= 10^4). Each of the following t lines contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
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
        
    #State: The output state will be the sum of the number of pairs (i, j) for each test case, where i is a positive integer less than or equal to a, and j is a positive integer greater than or equal to 4 and less than or equal to b, such that (j+i) is divisible by the greatest common divisor of i and j. The sum is calculated for each test case and printed separately.

#Overall this is what the function does:This function reads input from stdin, where the first line contains a positive integer T (1 <= T <= 10^4) representing the number of test cases. For each test case, it reads two positive integers n and m (1 <= n, m <= 2 * 10^6) and calculates the sum of the number of pairs (i, j) where i is a positive integer less than or equal to n, and j is a positive integer greater than or equal to 4 and less than or equal to m, such that (j+i) is divisible by the greatest common divisor of i and j. The function then prints the calculated sum for each test case, minus 1.

