#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: `x` is an integer between 0 and 50 (inclusive), `i` is equal to `x`, `n` is an integer between `x+1` and 50 (inclusive), `l` is a list of `n` distinct integers `p_1`, `p_2`, ..., `p_n` (1 <= `p_i` <= `n`; `p_i` != `i`), stdin contains `t-x-2` test cases, flag is True, and the number 2 is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n distinct integers. It then checks each list to see if there exists an integer p_i such that p_i is equal to the integer at index p_i - 1 in the list. If such an integer is found, it prints 2 and moves on to the next test case. If no such integer is found after checking all integers in the list, it prints 3. The function continues this process until all test cases have been processed.

