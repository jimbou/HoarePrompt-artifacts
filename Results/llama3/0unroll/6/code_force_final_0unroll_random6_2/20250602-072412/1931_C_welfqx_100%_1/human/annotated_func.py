#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: The output state will contain `t` lines, each representing the minimum number of operations required to make the corresponding input array `a_1`, `a_2`, ..., `a_n` a palindrome. If the input array is already a palindrome or has only one element, the output will be 0. Otherwise, the output will be the difference between the length of the array `n` and the maximum of `cn` and `ck`, where `cn` is the length of the longest prefix of the array that is a palindrome, and `ck` is the length of the longest suffix of the array that is a palindrome.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the minimum number of operations required to make each input array a palindrome. It accepts no parameters and returns no value, instead printing the results directly. The function takes an integer t, representing the number of test cases, followed by t test cases. Each test case consists of an integer n, representing the length of the array, and n integers a_1, a_2, ..., a_n. The function calculates the minimum number of operations required to make the array a palindrome and prints this value for each test case. If the input array is already a palindrome or has only one element, the output is 0. Otherwise, the output is the difference between the length of the array n and the maximum of the lengths of the longest prefix and suffix that are palindromes.

