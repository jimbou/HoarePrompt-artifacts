#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_i (1 <= p_i <= n; p_i != i).
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    if (n == 2) :
        print(2)
        #This is printed: 2
    else :
        for i in range(1, n + 1):
            if v[v[v[i]]] == i:
                print(2)
                return
            
        #State: n is an integer between 3 and 50 (inclusive), v is a list of n+1 integers where the first element is 0 and the remaining elements are the n distinct integers p_i (1 <= p_i <= n; p_i != i), i is n+1, stdin contains t-n test cases. If v[v[v[i]]] equals i, then 2 is printed. Otherwise, no output is produced.
    #State: *n is an integer between 2 and 50 (inclusive), v is a list of n+1 integers where the first element is 0 and the remaining elements are the n distinct integers p_i (1 <= p_i <= n; p_i != i) from the input, stdin contains t-1 test cases. If n equals 2, the integer 2 is being printed. If n is between 3 and 50 (inclusive), if v[v[v[i]]] equals i, then 2 is printed. Otherwise, no output is produced.

#Overall this is what the function does:This function reads input from stdin, processes a series of test cases, and prints output based on the conditions met. It accepts an integer t (1 <= t <= 5000) representing the number of test cases, followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) and n distinct integers p_i (1 <= p_i <= n; p_i != i). If n equals 2, it prints 2. For n between 3 and 50, it checks if v[v[v[i]]] equals i and prints 2 if true; otherwise, no output is produced. The function modifies the input list v and consumes input from stdin.

