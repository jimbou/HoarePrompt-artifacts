#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: `i` is `n`, `j` is 1 if `l` contains two consecutive elements `i + 2` and `i + 1` for any `i` in the range from 0 to `n - 1`, otherwise `j` is 0. If `j` is 0, the number 3 is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the result for each case. For each test case, it checks if a list of distinct integers contains two consecutive elements that are in reverse order (i.e., `i + 2` followed by `i + 1`). If such a pair is found, it prints 2; otherwise, it prints 3. The function iterates through all test cases and prints the corresponding results.

