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
            
        #State: The loop will print 2 and terminate as soon as it finds an index i such that v[v[v[i]]] equals i, or it will complete all iterations without printing anything if no such index is found. The value of i will be the index at which the loop terminated, or n+1 if the loop completed all iterations. The values of t, n, and v remain unchanged.
        print(3)
        #This is printed: 3
    #State: *stdin contains t-1 test cases, n is an integer between 2 and 50 inclusive, v is a list of n+1 integers where the first element is 0 and the remaining elements are the n distinct integers p_1, p_2, ..., p_n in the order they appeared in the input. If n equals 2, the number 2 is printed. If n is greater than 2, the loop will print 2 and terminate as soon as it finds an index i such that v[v[v[i]]] equals i, or it will complete all iterations without printing anything if no such index is found, and then the number 3 is printed.

#Overall this is what the function does:This function reads an integer n and a list of n distinct integers from standard input, then checks for a specific condition in the list. If n is 2, it prints 2. Otherwise, it iterates through the list to find an index i such that the value at the index v[v[i]] equals i. If such an index is found, it prints 2 and terminates. If no such index is found after iterating through the entire list, it prints 3. The function does not modify the input values or the list, and it does not return any value.

