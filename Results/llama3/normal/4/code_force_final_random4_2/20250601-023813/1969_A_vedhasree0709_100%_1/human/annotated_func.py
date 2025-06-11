#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_i (1 <= p_i <= n; p_i != i).
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: t is 0, n is an integer greater than 0, l is a list of n integers, i is n, p is the (n-1)th element of l, q is the (p-1)th element of l, j is either 1 or 0, stdin is empty. If j is 0, the number 3 is being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n distinct integers. It then checks for a specific condition in each test case: if there exists a pair of integers p and q such that q is equal to p's index plus one, it prints 2. If no such pair is found, it prints 3. The function continues this process until all test cases have been processed, at which point the standard input is empty.

