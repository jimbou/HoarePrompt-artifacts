#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 2 * 10^4). Each test case contains two lines. The first line of each test case contains a single integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: Output State: `_` is equal to the number of test cases `t`, `stdin` contains 0 inputs, and `n`, `arr`, `mpp`, `i`, and `first` are in the same state as after the last iteration of the loop.
    #
    #In natural language, this output state means that the loop has finished executing all the test cases provided in the input. The variable `_` has been incremented to the total number of test cases `t`, and the standard input `stdin` is empty, indicating that all test cases have been processed. The variables `n`, `arr`, `mpp`, `i`, and `first` retain their values from the last iteration of the loop, as they are not modified after the loop finishes executing.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a list of integers. For each test case, it finds and prints the smallest positive integer that is either missing from the list or appears only once. The function processes all test cases and leaves the standard input empty.

