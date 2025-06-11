#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_i (1 <= p_i <= n; p_i != i).
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
        
    #State: `n` is an integer between 2 and 50 inclusive, `i` is equal to `n`, `x` is an integer, `l` is a list of integers, stdin is empty, and `flag` is True if `l[l[i] - 1]` is equal to `l[i] - 1` for any `i` in the range of `x`, otherwise `flag` is not defined.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the result of each test case. For each test case, it reads an integer x and a list of x distinct integers, then checks if any integer in the list is equal to the integer at the index specified by the integer minus one. If such a pair is found, it prints 2; otherwise, it prints 3. The function does not return any value but modifies the stdin by consuming the input.

