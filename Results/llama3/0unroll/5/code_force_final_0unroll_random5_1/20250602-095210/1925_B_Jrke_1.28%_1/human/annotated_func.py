#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        if k == 1:
            print(1)
            continue
        
        ans = 1
        
        for i in range(1 + (1 if x % 2 == 0 else 0), int(x ** 0.5) + 1, 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: The output state will contain t lines, each containing the maximum divisor of x that is less than or equal to k, where k is the integer division of x by n. If k is 1, the output will be 1. Otherwise, the output will be the maximum divisor of x that is less than or equal to k, considering only odd divisors (since the inner loop iterates over odd numbers).

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers x and n. For each case, it calculates the maximum divisor of x that is less than or equal to the integer division of x by n, considering only odd divisors if the integer division is greater than 1. The function then prints the result for each test case.

