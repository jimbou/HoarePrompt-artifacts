#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n + 1):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: `n` is at least 0, `i` is `n`, `arr` is a list of integers, `mpp` is a dictionary containing the frequency of each integer in `arr`, `stdin` contains no test cases, `_` is the number of test cases minus 1, `first` is True if there exists a key `k` in `mpp` such that `mpp[k]` is 1, otherwise `first` is False.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a list of integers. It then finds and prints the smallest positive integer that is either missing from the list or appears only once, if such an integer exists. If no such integer is found, it prints the smallest positive integer that is greater than the length of the list. The function processes all test cases and prints the result for each case.

