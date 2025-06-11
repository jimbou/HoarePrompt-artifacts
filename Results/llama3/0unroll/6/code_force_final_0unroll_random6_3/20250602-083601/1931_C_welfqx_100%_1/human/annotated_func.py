#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    t = int(input())
    for r in range(t):
        n = int(input())
        
        f = 1
        
        num = [int(_) for _ in input().split()]
        
        for j in range(n - 1):
            if num[j] != num[j + 1]:
                f = 0
                break
        
        if n == 1 or f == 1:
            print(0)
            continue
        
        onum = num.copy()
        
        onum.reverse()
        
        cn = 1
        
        ck = 1
        
        f = 1
        
        symb1 = num[0]
        
        symb2 = onum[0]
        
        for i in range(n - 1):
            if num[i] == num[i + 1]:
                cn += 1
            else:
                break
        
        for ii in range(n - 1):
            if onum[ii] == onum[ii + 1]:
                ck += 1
            else:
                break
        
        if symb1 == symb2:
            cn += ck
        
        print(n - max(cn, ck))
        
    #State: The loop will print t-1 lines, each containing a single integer. The integer on each line represents the minimum number of operations required to make the corresponding test case array a palindrome. The value of t remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the minimum number of operations required to make each test case array a palindrome. It accepts an integer t (1 <= t <= 10^4) followed by t test cases, each consisting of an integer n (1 <= n <= 2 * 10^5) and n integers a_1, a_2, ..., a_n (1 <= a_i <= n). The function returns t lines, each containing a single integer representing the minimum number of operations required to make the corresponding test case array a palindrome.

