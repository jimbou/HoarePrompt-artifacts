#State of the program right berfore the function call: stdin contains t+1 lines of input. The first line contains one integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: The output state will contain t lines of output, each containing the minimum of two calculated values: ans1 (a * n) and ans2 (b * n // 2 + a * n % 2), or just a if n is 1. The values of t, n, a, and b from the initial state are not changed.

#Overall this is what the function does:This function reads a series of input lines from standard input, where the first line contains an integer t representing the number of test cases, and each subsequent line contains three integers n, a, and b. For each test case, it calculates two values, ans1 and ans2, based on the input values, and prints the minimum of these two values. If n is 1, it simply prints the value of a. The function does not modify the input values and produces t lines of output, each containing the calculated minimum value or the value of a for n=1.

