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
            
        #State: The loop will either print 2 and terminate, or it will finish all iterations without printing anything. In the latter case, the state of the variables will remain unchanged, i.e., n is an integer between 3 and 50 (inclusive), v is a list of n+1 integers where the first element is 0 and the remaining elements are n distinct integers between 1 and n (inclusive) in the order they appeared in the input, and stdin contains t-1 test cases.
        print(3)
        #This is printed: 3
    #State: *n is an integer between 2 and 50 (inclusive), v is a list of n+1 integers where the first element is 0 and the remaining elements are n distinct integers between 1 and n (inclusive) in the order they appeared in the input, stdin contains t-1 test cases. If n is 2, the number 2 is printed. If n is not 2, either the number 2 is printed and the loop terminates, or the loop completes all iterations without printing anything, in which case the state of the variables remains unchanged and the number 3 is printed.

#Overall this is what the function does:This function reads an integer n and a list of n distinct integers from standard input, then checks for a specific condition in the list. If n is 2, it prints 2. Otherwise, it checks if there exists an integer i such that the value at index v[v[i]] equals i. If such an integer is found, it prints 2. If no such integer is found after checking all elements, it prints 3. The function does not modify the input values or store any results; it only prints a single integer based on the input.

