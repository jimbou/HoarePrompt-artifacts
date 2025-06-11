#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (3 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
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
        
    #State: The output state will contain t lines, each containing either 'YES' or 'NO'. 'YES' indicates that the given sequence of integers can be reduced to zero by the described operations, and 'NO' indicates that it cannot.

#Overall this is what the function does:This function determines whether a given sequence of integers can be reduced to zero by a specific set of operations. It reads a number of test cases, and for each test case, it reads a sequence of integers. It then applies the operations to the sequence, checking if it can be reduced to zero. If the sequence can be reduced to zero, it prints 'YES', otherwise it prints 'NO'. The function handles multiple test cases and provides a separate output for each case.

