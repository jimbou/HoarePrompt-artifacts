#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_i (1 <= p_i <= n; p_i != i).
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
        
    #State: n is an integer between 2 and 50 inclusive and must be at least x+t-1, x is an integer between 2 and 50 inclusive and must be at least x+t-1, l is a list of n distinct integers, i is x, flag is True, stdin contains 0 test cases, the number 2 or 3 was printed. If l[l[i] - 1] equals i + 1 for any i in the range [0, x) then flag is True, the number 2 is printed, and we break out of the most internal loop or if statement. Otherwise, nothing happens.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n distinct integers. It then checks if there exists an integer p_i in the list such that p_i equals the index i + 1. If such an integer is found, it prints 2 and breaks out of the loop. If no such integer is found, it prints 3. The function repeats this process for all test cases and then terminates.

