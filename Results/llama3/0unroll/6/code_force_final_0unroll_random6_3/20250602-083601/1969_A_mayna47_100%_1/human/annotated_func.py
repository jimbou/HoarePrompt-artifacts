#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines: the first line contains one integer n (2 <= n <= 50), and the second line contains n integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i; all p_i are distinct).
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: The loop will print 2 and terminate as soon as it finds an index i such that the value at index v[i] in list v is equal to i. If no such index is found, the loop will complete all iterations without printing anything. The value of n and the list v remain unchanged.
    print(3)
    #This is printed: 3

#Overall this is what the function does:Determines whether a given permutation of integers contains a pair of elements that are each other's inverse, and prints 2 if such a pair is found, or 3 if no such pair exists.

