#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: The output state will contain t lines, each representing the minimum number of consecutive occurrences of a number in the corresponding test case. If no such number exists, the output will be -1. The output will be in the same order as the input test cases.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints output to standard output. It accepts a series of test cases, where each test case consists of an integer n followed by a list of n integers. The function then analyzes each test case to find the minimum number of consecutive occurrences of a number in the list. If such a number exists, it prints the minimum count; otherwise, it prints -1. The output is presented in the same order as the input test cases.

