#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf:
            print(-1)
        else:
            print(minn)
        
    #State: `n` is an integer greater than or equal to 1, `ar` is a list of `n` integers, `same` is 1, `num` is the last integer in `ar`, `i` is `n`, and stdin contains 0 test cases. If `minn` is infinite, -1 is printed. Otherwise, the minimum of the original `minn` and 1 is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then finds the minimum number of consecutive occurrences of the same integer in each test case. If no such occurrences are found, it prints -1; otherwise, it prints the minimum number of consecutive occurrences. The function processes all test cases and prints the results accordingly.

