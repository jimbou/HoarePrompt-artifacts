#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
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
            
        #State: The loop will print 2 and terminate as soon as it finds an index i such that v[v[v[i]]] equals i. If no such index is found after iterating over all indices from 1 to n, the loop will finish without printing anything. The value of n and the list v remain unchanged.
        print(3)
        #This is printed: 3
    #State: *stdin contains t-1 test cases, n is an integer between 2 and 50 inclusive, v is a list of n+1 integers where the first element is 0 and the remaining elements are the n distinct integers from the second line of the test case, with each integer between 1 and n inclusive and not equal to its 1-based index. If n equals 2, then 2 is printed. Otherwise, the loop will print 2 and terminate as soon as it finds an index i such that v[v[v[i]]] equals i. If no such index is found after iterating over all indices from 1 to n, the loop will finish without printing anything, and the number 3 is being printed.

#Overall this is what the function does:This function reads a test case from standard input, where the test case consists of an integer n and a list of n distinct integers. It then checks for a specific condition in the list, and if the condition is met, it prints 2. If the condition is not met and n is not equal to 2, it prints 3. If n is equal to 2, it only prints 2. The function does not modify the input values and does not return any value, only printing the result to the standard output.

