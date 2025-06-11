#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == i + 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: `n` is greater than or equal to 0, `i` is equal to `n`, `x` is an integer, `l` is a list of integers, stdin contains no more test cases. If there exists an index `j` in the range `[0, x)` such that `l[l[j] - 1]` equals `j + 1` for any iteration of the loop, then `flag` is True and the number 2 is printed for that iteration. Otherwise, the number 3 is printed for that iteration.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n distinct integers. It checks for each test case if there exists an index j such that the jth integer is equal to the index of the jth integer plus one. If such an index exists, it prints 2; otherwise, it prints 3. The function processes all test cases and then terminates, leaving the standard input empty.

