#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 100). Each of the following t lines contains two integers n and m (1 <= n, m <= 100).
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        
        if n == m:
            print('Yes')
        elif m > n:
            print('No')
        elif m == n - 1:
            print('Yes')
        elif m % 2 == 0 and n % 2 == 0:
            print('Yes')
        elif m % 2 != 0 and n % 2 != 0:
            print('Yes')
        else:
            print('No')
        
    #State: The loop has executed `t` times, and for each iteration, it has printed 'Yes' or 'No' to the console based on the conditions specified in the loop body. The values of `n` and `m` have been read from the input and used in the conditions, but they do not persist after each iteration. The final state is that the loop has finished executing, and the program has terminated.

#Overall this is what the function does:This function reads a series of input lines from the standard input, where the first line contains an integer t, representing the number of test cases, and each subsequent line contains two integers n and m. It then evaluates the relationship between n and m for each test case, printing 'Yes' if n and m are equal, or if m is one less than n, or if both n and m are even or both odd. Otherwise, it prints 'No'. The function does not return any value, but instead, prints the results directly to the console, and its execution terminates after processing all test cases.

