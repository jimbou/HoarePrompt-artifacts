#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 ≤ t ≤ 10^3) and then t pairs of integers x and n (1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x).
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: t is an integer (0 ≤ t ≤ 10^3), x is an integer (1 ≤ x ≤ 10^8), n is an integer (1 ≤ n ≤ x), ans is the maximum of the previous value of ans and x // i if n is less than or equal to x // i, otherwise ans is the maximum of the previous value of ans and i if n is less than or equal to i, stdin contains t-1 inputs: t-1 pairs of integers x and n (1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x), i is isqrt(x) + 1.
    print(ans)
    #This is printed: the maximum value of ans (where ans is the maximum of the previous value of ans and x // i if n is less than or equal to x // i, otherwise ans is the maximum of the previous value of ans and i if n is less than or equal to i)

#Overall this is what the function does:This function reads input from stdin, where the first input is an integer t, followed by t pairs of integers x and n. For each pair, it calculates the maximum divisor of x that is less than or equal to n, and prints this value. The function iterates through all pairs of integers, processing each pair independently, and outputs the maximum divisor for each pair.

