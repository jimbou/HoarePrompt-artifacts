#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an integer between 0 and 10^4, stdin is empty. For each line of input that was read, 'Yes' is printed if either `a` or `b` (or both) is even, otherwise 'No' is printed.

#Overall this is what the function does:This function reads a series of lines from standard input, where the first line contains a single integer t, and each subsequent line contains two integers a and b. It then checks each pair of integers to determine if either a or b (or both) is even, printing 'Yes' if so, and 'No' otherwise. The function processes all input lines and prints a corresponding output for each pair of integers, leaving the standard input empty after execution.

