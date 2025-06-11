#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n, then a list of n integers. The list is a beautiful array.
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
        
    #State: The output state will contain t lines, each containing a single integer. This integer will be the minimum number of consecutive occurrences of the same number in the beautiful array. If no such number exists, the output will be -1.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then analyzes each list to find the minimum number of consecutive occurrences of the same number. If such a number exists, it prints the minimum count; otherwise, it prints -1. The function processes multiple test cases and outputs the result for each case on a separate line.

