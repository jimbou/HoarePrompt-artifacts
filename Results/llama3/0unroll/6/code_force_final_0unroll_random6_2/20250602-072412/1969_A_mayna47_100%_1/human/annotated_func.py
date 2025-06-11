#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: The loop will print 2 and terminate if it finds a pair of elements in the list v that are swapped with each other, i.e., v[v[i]] == i for some i. If no such pair is found, the loop will complete all iterations without printing anything. The value of n remains unchanged, and the list v remains unchanged as well, as the loop only reads from it and does not modify it.
    print(3)
    #This is printed: 3

#Overall this is what the function does:This function reads an integer n and a list of n distinct integers from standard input, then checks if there exists a pair of elements in the list that are swapped with each other. If such a pair is found, it prints 2 and terminates. If no such pair is found after checking all elements, it prints 3. The function does not modify the input list or the value of n.

