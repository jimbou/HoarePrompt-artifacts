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
        
    #State: t is an integer from stdin, n is an integer from stdin, l is a list of integers from stdin, i is n, j is 1 if there exists an index p such that l[p - 1] is equal to p, otherwise j is 0, p is the element of l at index n - 1, q is the element of l at index p - 1, where p is the element of l at index n - 1, _ is t, stdin is empty. If there does not exist an index p such that l[p - 1] is equal to p, the number 3 is printed t times. If there exists an index p such that l[p - 1] is equal to p, the number 2 is printed t times.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n distinct integers. It then checks for each test case if there exists an index p such that the element at index p-1 is equal to p. If such an index exists, it prints 2; otherwise, it prints 3. The function repeats this process for all test cases and does not return any value.

