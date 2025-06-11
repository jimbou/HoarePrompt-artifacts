#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
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
        
    #State: The output state will be a series of numbers, either 2 or 3, each on a new line, depending on the input values. For each test case, if there exists an index i such that the value at index i in the list is equal to i+1, then the output will be 2. Otherwise, the output will be 3. The number of output lines will be equal to the number of test cases (t-1).

#Overall this is what the function does:This function reads input from standard input, processes multiple test cases, and outputs a series of numbers (either 2 or 3) based on the input values. For each test case, it checks if there exists an index i such that the value at index i in the list is equal to i+1. If such an index exists, it outputs 2; otherwise, it outputs 3. The function processes a variable number of test cases, as specified by the initial input, and produces a corresponding number of output lines.

