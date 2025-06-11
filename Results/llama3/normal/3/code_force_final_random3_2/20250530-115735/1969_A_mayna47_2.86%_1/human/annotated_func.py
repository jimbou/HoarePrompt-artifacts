#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
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
            
        #State: `stdin` contains t-1 test cases, `n` is an integer between 3 and 50 inclusive, `v` is a list of n+1 integers where the first element is 0 and the remaining elements are the n distinct integers p_1, p_2, ..., p_n, `i` is n, and if `v[v[v[i]]]` equals `i` for any `i` in the range from 1 to `n`, the number 2 is printed.
    #State: *stdin contains t-1 test cases, n is an integer between 2 and 50 inclusive, v is a list of n+1 integers where the first element is 0 and the remaining elements are the n distinct integers p_1, p_2, ..., p_n. If n equals 2, the number 2 is printed. If n is between 3 and 50 inclusive, and if v[v[v[i]]] equals i for any i in the range from 1 to n, the number 2 is printed.

#Overall this is what the function does:This function reads an integer n and a list of n distinct integers from standard input, and checks if there exists a cycle of length 2 in the permutation represented by the list. If n is 2, it prints 2. If n is greater than 2, it checks for a cycle of length 2 by iterating through the list and checking if the permutation of the permutation of each element is equal to the element itself. If such a cycle is found, it prints 2.

