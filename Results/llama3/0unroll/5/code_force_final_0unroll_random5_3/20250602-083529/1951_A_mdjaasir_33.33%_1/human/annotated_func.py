#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= t <= 1000) and then a binary string of size n (1 <= n <= 50).
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = input()
        
        count = a.count('1')
        
        if count == 0:
            print('YES')
        elif count > 2 and count % 2 == 0:
            print('YES')
        elif count == 2:
            if a.index('1') and a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: The loop will execute t times, each time reading a binary string of size n from stdin, and printing 'YES' or 'NO' to stdout based on the count of '1's in the string and their positions. After all iterations, the loop will terminate, leaving the value of t unchanged.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer and a binary string. It then checks the count of '1's in the binary string and their positions, printing 'YES' if the count is 0, or if the count is greater than 2 and even, or if the count is 2 and the '1's are not adjacent. Otherwise, it prints 'NO'. The function repeats this process for the specified number of test cases, leaving the input value unchanged after execution.

