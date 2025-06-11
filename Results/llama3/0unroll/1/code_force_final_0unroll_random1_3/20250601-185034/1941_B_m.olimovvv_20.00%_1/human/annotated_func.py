#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (3 <= n <= 2 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: The output state is a series of 'YES' or 'NO' strings, each corresponding to a test case. If the first and second elements of the list or the last and second last elements of the list do not satisfy the given conditions, the output is 'NO', otherwise it is 'YES'. The number of 'YES' or 'NO' strings is equal to the number of test cases t.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then checks if the first and second elements or the last and second last elements of the list satisfy certain conditions (specifically, if the first and last elements are odd and the second element is not two more than the first, or the second last element is not two more than the last). If these conditions are not met, it prints 'NO', otherwise it prints 'YES'. The function repeats this process for each test case and outputs a series of 'YES' or 'NO' strings corresponding to each test case.

