#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^5), followed by two strings s and f of length n, consisting of '0' and '1' characters.
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        a = b = 0
        
        for i in range(n):
            a += s[i] > t[i]
            b += s[i] < t[i]
        
        print(max(a, b))
        
    #State: stdin is empty, t is 0, n is an integer between 1 and 10^5, s is a string of length n consisting of '0' and '1' characters, t is a string of length n consisting of '0' and '1' characters, a is 0, b is 0, _ is t, i is n.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of an integer n and two binary strings s and t of length n. For each test case, it calculates the maximum number of positions where s is greater than t or s is less than t, and prints this maximum value. The function consumes all input from standard input and leaves it empty.

