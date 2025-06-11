#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_i (1 <= p_i <= n; p_i != i).
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
        
    #State: `n` is an integer equal to the first input, `l` is a list of integers equal to the second input, `i` is equal to `n`, `j` is either 0 or 1. If `j` is 0, then there does not exist an index `k` such that `l[k]` is equal to `k + 2` and `l[k + 1]` is equal to `k + 1`, and the number 3 is printed. If `j` is 1, then there exists an index `k` such that `l[k]` is equal to `k + 2` and `l[k + 1]` is equal to `k + 1`, and the number 2 is printed. In both cases, stdin is empty.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n distinct integers. It then checks for a specific condition in each test case: if there exists a pair of adjacent integers where the first integer is equal to its 1-based index plus 2 and the second integer is equal to its 1-based index plus 1, it prints 2; otherwise, it prints 3. The function processes all test cases and empties the standard input.

