#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: The output state will be a list of integers, where each integer represents the result of each test case. The result will be either 2 or 3, depending on whether a pair of integers in the input list satisfies the condition q == i + 1. If such a pair is found, the result will be 2; otherwise, the result will be 3. The number of integers in the output list will be equal to the number of test cases, which is given by the integer t in the initial state.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a list of distinct integers. It checks each list for a specific condition: whether there exists a pair of integers where the value of the second integer is equal to the index of the first integer plus one. If such a pair is found, it prints 2; otherwise, it prints 3. The function processes multiple test cases and prints the result for each case.

