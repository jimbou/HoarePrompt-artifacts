#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t, then for each test case, first an integer n and then a list of n integers. The integers are positive and less or equal to n.
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
        
    #State: t is a positive integer greater than or equal to 0, r is equal to t, n is greater than or equal to 1, f is 1, num is a list of n positive integers less than or equal to n, j is n - 1, onum is a reversed copy of num, stdin contains 0 inputs, i is n - 1, ck is either 1 or greater than or equal to 2 and less than or equal to n - 1, cn is greater than or equal to 1 plus ck, and ii is n - 1. If the current value of onum[ii] is equal to the current value of onum[ii + 1], then ck is greater than or equal to 2 and less than or equal to n - 1. Otherwise, ck is 1 and we break out of the most internal loop or if statement. If the first element of num is equal to the first element of num, then cn is greater than or equal to 1 plus ck. The value of n minus the maximum of cn and ck is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n positive integers. It then checks if the list is already sorted or if it can be sorted by reversing a contiguous subsequence of the list. If the list is already sorted or can be sorted by reversing a subsequence, it prints 0. Otherwise, it prints the minimum number of elements that need to be reversed to sort the list. The function repeats this process for each test case.

