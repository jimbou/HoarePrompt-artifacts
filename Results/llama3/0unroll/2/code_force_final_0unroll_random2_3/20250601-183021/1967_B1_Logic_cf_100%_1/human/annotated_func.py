#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: The output state will contain t lines, each containing a single integer. The integer on each line represents the sum of the number n and the number of multiples of each integer b from 2 to min(n, m) that are less than or equal to n.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts no parameters and returns no value. The function reads a series of lines from stdin, where the first line contains an integer t, representing the number of test cases. Each subsequent line contains two positive integers n and m. For each test case, the function calculates a sum of n and the number of multiples of each integer b from 2 to min(n, m) that are less than or equal to n, and prints this sum as a single integer on a new line. The function repeats this process for all t test cases, resulting in t lines of output.

