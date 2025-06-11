#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (3 <= n <= 2 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        for i in range(0, a - 2):
            if b[i] < 0:
                print('NO')
                break
            b[i + 1] -= b[i] * 2
            b[i + 2] -= b[i]
            b[i] -= b[i]
        else:
            if b[-1] != 0 or b[-2] != 0:
                print('NO')
            else:
                print('YES')
        
    #State: a is an integer between 3 and 2 * 10^5 inclusive, b is a list of a integers, for all j in range(0, a - 2), the current value of b[j] is 0, the current value of b[a - 1] is b[a - 1] - (a - 2) * b[0] - 2 * b[i], the current value of b[a - 2] is b[a - 2] - (a - 3) * b[0] - b[i], b[i] is 0, b[i + 1] is b[i + 1] - 2 * b[i], b[i + 2] is b[i + 2] - b[i], i is a - 2, stdin contains t-3 test cases, each consisting of an integer n followed by a list of n integers a_1, a_2, ..., a_n, t is at least 3.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then processes each test case by iterating through the list of integers, modifying the values in the list based on certain conditions, and finally prints 'YES' if the last two integers in the list are zero after processing, and 'NO' otherwise. The function continues to read and process test cases until it has processed all the input provided.

