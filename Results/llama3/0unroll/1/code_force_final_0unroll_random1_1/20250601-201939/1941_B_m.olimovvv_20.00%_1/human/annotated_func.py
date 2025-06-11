#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the next t lines contains an integer n (3 <= n <= 2 * 10^5), followed by a line containing n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, each corresponding to the input test cases. The number of 'YES' or 'NO' will be equal to the number of test cases (t) provided in the input.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer 'n' followed by 'n' integers. It then checks if the first and last numbers in the sequence have certain properties (specifically, if they are odd and the preceding or succeeding number is not 2 more than them). Based on this check, it prints 'YES' or 'NO' to the console for each test case, indicating whether the sequence meets the specified conditions.

