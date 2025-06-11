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
        
    #State: The output state is a series of integers, each representing the maximum divisor of x that is less than or equal to k, where k is the integer division of x by n. The number of integers in the output state is equal to the value of t, which is the first integer in the initial state.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers x and n. For each test case, it calculates the maximum divisor of x that is less than or equal to the integer division of x by n, and prints this value. The function repeats this process for each test case, producing a series of output integers equal in number to the initial test case count.

