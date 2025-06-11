#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a positive integer t (1 <= t <= 10^4). Each test case contains two positive integers n, m (1 <= n, m <= 2 * 10^6) on a single line.
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
        
    #State: The output state is the sum of the calculated values for each test case, where each value is the sum of the positive divisors of the number a minus the sum of the positive divisors of the number b, minus 2. The output is printed for each test case.

#Overall this is what the function does:This function calculates and prints the sum of the differences between the sum of positive divisors of two numbers, 'a' and 'b', minus 2, for multiple test cases provided as input. It takes no parameters and returns no value, instead printing the calculated sums for each test case.

