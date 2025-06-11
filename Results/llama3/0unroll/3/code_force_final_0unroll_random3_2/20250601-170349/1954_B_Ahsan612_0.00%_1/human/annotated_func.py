#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: The output state contains t lines, each containing the minimum number of consecutive occurrences of the same number in the corresponding list of integers. If no such number exists, the output is -1.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the minimum number of consecutive occurrences of the same number in each list of integers. For each test case, it iterates through the list, tracking the count of consecutive occurrences of the same number, and updates the minimum count if a smaller count is found. If no consecutive occurrences are found, it outputs -1. The function processes all test cases and prints the minimum count for each case.

