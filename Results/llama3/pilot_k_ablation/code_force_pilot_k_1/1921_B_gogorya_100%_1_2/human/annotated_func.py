#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^5) followed by two strings s and f of length n, consisting of characters '0' and '1'.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s1 = input()
        
        s2 = input()
        
        hd = 0
        
        for i in range(n):
            if s1[i] != s2[i]:
                hd += 1
        
        res = abs(s1.count('1') - s2.count('1'))
        
        print(res + abs(hd - res) // 2)
        
    #State: t is 0, _ is t, n is an integer, s1 is a string, s2 is a string, hd is the number of positions at which the corresponding characters of s1 and s2 are different in the last test case, res is the absolute difference between the number of '1's in s1 and s2 in the last test case, stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two binary strings of equal length. It calculates the minimum number of operations required to make the two strings identical, where an operation is either flipping a bit or swapping two bits. The function prints the result for each test case and consumes all input from standard input, leaving it empty.

