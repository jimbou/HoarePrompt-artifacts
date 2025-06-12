#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines. The first line contains an integer n (1 <= n <= 10^5). The second and third lines contain two strings s and f of length n, consisting of '0's and '1's. The sum of n over all test cases does not exceed 10^5.
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        a = b = 0
        
        for i in range(n):
            a += s[i] > t[i]
            b += s[i] < t[i]
        
        print(max(a, b))
        
    #State: `stdin` is empty, `t` is 0, `n` is 0, `s` is an empty string, `t` is an empty string, `a` is 0, `b` is 0, `_` is `t` (the initial value of `t`), and the maximum of `a` and `b` has been printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and two binary strings s and t of length n. It then compares the strings character by character, counting the number of positions where s is greater than t (a) and the number of positions where s is less than t (b). Finally, it prints the maximum of a and b for each test case, effectively determining the maximum number of positions where one string is lexicographically greater than the other.

