#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n % 2:
            if 2 * a < b:
                print(a * n)
            else:
                print(n // 2 * b + a)
        elif 2 * a < b:
            print(a * n)
        else:
            print(n // 2 * b)
        
    #State: The output state will be a list of integers, each representing the result of the calculation for the corresponding input line. The calculation depends on the values of n, a, and b. If n is odd, the result is either a*n if 2*a < b, or n//2 * b + a otherwise. If n is even, the result is a*n if 2*a < b, or n//2 * b otherwise.

#Overall this is what the function does:Calculates and prints the result of a mathematical operation for each input line, based on the values of n, a, and b. The operation depends on whether n is odd or even, and the relationship between a and b. For odd n, the result is either a*n if 2*a < b, or n//2 * b + a otherwise. For even n, the result is a*n if 2*a < b, or n//2 * b otherwise. The function processes multiple input lines and prints the result for each line.

