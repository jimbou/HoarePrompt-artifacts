#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and (x - n * (x // i)) % (x //
                    i) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: The output state will contain t lines, each containing the maximum possible value of ans for the corresponding input values of x and n.

#Overall this is what the function does:This function reads a series of input pairs (x, n) from standard input, where x and n are integers, and for each pair, it calculates and prints the maximum possible value of a divisor i of x such that x - n*i is a multiple of i and non-negative. The function processes multiple test cases, as specified by an initial integer t, and outputs the maximum possible value for each test case.

