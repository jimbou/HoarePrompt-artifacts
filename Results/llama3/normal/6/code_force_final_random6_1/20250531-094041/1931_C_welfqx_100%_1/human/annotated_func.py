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
        
    #State: t is 0, r is t, stdin is empty, n is an integer between 1 and 2 * 10^5, f is 1, num is a list of n integers between 1 and n, j is n - 1, onum is a reversed copy of num, ck is the length of the longest contiguous sequence of equal elements starting from the first element of num, symb1 is the first element of num, symb2 is the last element of num, i is n - 1, and ii is n - 1. If the first element of num is equal to the last element of num, then cn is twice the length of the longest contiguous sequence of equal elements starting from the first element of num. The difference between the number of elements in the list num and the maximum of cn and ck is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. It then analyzes each list to find the maximum length of contiguous sequences of equal elements at the beginning and end of the list. If the first and last elements of the list are equal, it combines these sequences. Finally, it prints the difference between the total number of elements in the list and the maximum length of these sequences.

