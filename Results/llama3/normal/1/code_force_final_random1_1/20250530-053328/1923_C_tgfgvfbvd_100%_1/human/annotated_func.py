#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 10^4), followed by t test cases. Each test case consists of two integers n and q (1 <= n, q <= 3 * 10^5), followed by n integers c_1, c_2, ..., c_n (1 <= c_i <= 10^9), followed by q lines, each containing two integers l_i and r_i (1 <= l_i <= r_i <= n).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [0]
        
        c = [0]
        
        i, j = 0, 0
        
        for x in l:
            if x == 1:
                j += 1
            i += x
            p.append(i)
            c.append(j)
        
        for _ in range(m):
            a, b = map(int, input().split())
            i = c[b] - c[a - 1]
            s = p[b] - p[a - 1]
            if b - a + 1 > 1 and s - (b - a + 1) >= i:
                print('YES')
            else:
                print('NO')
        
    #State: n is an integer between 1 and 3 * 10^5, m is an integer greater than 0, l is a list containing m elements, p is a list containing m+1 elements, c is a list containing m+1 elements, stdin contains 0 test cases, a is an integer, b is an integer, s is the difference between the bth and (a-1)th elements of list p, i is the difference between the bth and (a-1)th elements of list c, j is the count of 1's in list l, _ is m - 1, and x is the last element in the list. If b - a + 1 > 1 and s - (b - a + 1) >= i, then 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints 'YES' or 'NO' for each test case based on certain conditions. It accepts no parameters and returns no value. The function's purpose is to determine whether a given condition is met for each test case and print the corresponding result. The final state of the program is that stdin is empty, and the function has printed 'YES' or 'NO' for each test case.

