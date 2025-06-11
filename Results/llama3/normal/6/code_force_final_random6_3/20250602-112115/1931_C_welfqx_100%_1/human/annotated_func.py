#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the length of the list. The list contains positive integers. The sum of the lengths of all lists does not exceed 2 * 10^5.
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
        
    #State: t is a positive integer, r is t - 1, n is at least 1, f is 1, num is a list of positive integers, j is n - 1, onum is a reversed copy of num, i is n - 1, ii is n - 1, symb1 is the first element of num, symb2 is the first element of the reversed num, cn is either n or the number of consecutive equal elements starting from the first element of num, ck is either n or the number of consecutive equal elements starting from the last element of num. If the first element of num (symb1) is equal to the last element of num (symb2), then cn is either 2n - 1 or the sum of the number of consecutive equal elements starting from the first element of num and the number of consecutive equal elements starting from the last element of num. The difference between n and the maximum of cn and ck is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n followed by a list of n positive integers. It then checks if all elements in the list are equal. If they are, or if the list contains only one element, it prints 0. Otherwise, it counts the number of consecutive equal elements starting from the first and last elements of the list, and prints the difference between the length of the list and the maximum of these two counts.

