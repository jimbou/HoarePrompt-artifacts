#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: The loop will either print 2 and terminate early, or it will complete all iterations without printing anything. In the latter case, the state of the variables will remain unchanged, i.e., n will still be an integer between 1 and 5000, and v will still be a list of n+1 integers where the first element is 0 and the rest are distinct integers between 1 and n. The stdin will still contain t-1 test cases.
    print(3)
    #This is printed: 3

#Overall this is what the function does:This function reads input from stdin, processes it, and prints either 2 or 3. It accepts no parameters and returns no value. The function's purpose is to determine whether a given set of distinct integers satisfies a specific condition. If the condition is met, it prints 2 and terminates early. Otherwise, it prints 3. The function's final state is that it has processed one test case from stdin and printed a result, leaving the remaining test cases in stdin unchanged.

