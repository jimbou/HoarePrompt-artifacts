#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The output state will be the input state with the variable `n` decremented by 1, and the rest of the test cases (t-1 test cases) and the integers p_1, p_2, ..., p_n for the current test case consumed from stdin. The output will contain either 2 or 3 for each test case, depending on whether the condition `l[l[i] - 1] == l[i] - 1` is met.

#Overall this is what the function does:This function reads input from stdin, processes test cases, and outputs a result for each case. It accepts no parameters and returns no value. The function reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of an integer n and n distinct integers. The function checks if any of the integers p_i is equal to the integer at index p_i - 1 in the list. If such a condition is met, it prints 2; otherwise, it prints 3. The function consumes the input for the current test case and the remaining test cases (t-1 test cases) from stdin, leaving the input state with the variable `n` decremented by 1.

