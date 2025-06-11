#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (3 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: a is an integer equal to 0, b is an empty list, stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then checks if the first and last integers in each test case meet certain conditions (specifically, if they are odd and not part of a sequence with a difference of 2). If the conditions are not met, it prints 'NO', otherwise it prints 'YES'. After processing all test cases, the function leaves the input stream empty and the variables a and b in a neutral state (a=0, b=[]).

