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
        
    #State: a is 0, b is a list of t integers with b[i] equal to 0, b[i + 1] decreased by (a - 1) times the original value of b[i], and b[i + 2] decreased by the original value of b[i], _ is t, i is a - 1, and stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains an integer n followed by n integers. It then performs a series of operations on the integers, subtracting multiples of the first integer from the subsequent integers. If all integers in the test case become zero after these operations, the function prints 'YES', otherwise it prints 'NO'. The function repeats this process for all test cases and then terminates, leaving the input stream empty.

