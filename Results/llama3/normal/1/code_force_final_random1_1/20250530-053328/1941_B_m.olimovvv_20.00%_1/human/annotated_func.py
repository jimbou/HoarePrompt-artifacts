#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (3 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: a is an integer equal to 0, b is an empty list, stdin is empty. Either 'NO' or 'YES' is printed for each test case.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines whether a given sequence of integers meets certain conditions. For each test case, it checks if the first and last elements of the sequence satisfy specific parity and difference requirements. If the conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and then terminates, leaving stdin empty and the input variables in a reset state.

