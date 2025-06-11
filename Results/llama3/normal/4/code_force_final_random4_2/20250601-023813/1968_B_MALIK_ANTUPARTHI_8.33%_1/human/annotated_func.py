#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 2 * 10^5) followed by two binary strings a and b of lengths n and m, respectively.
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e.index(d[j]) + 1
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: a is an integer between 1 and 10^4 inclusive, stdin contains 0 test cases, b is an integer greater than or equal to 0 and less than or equal to 2*10^5 inclusive, c is an integer between 1 and 2*10^5 inclusive, d is a binary string of length b, e is a binary string of length c, i is a, j is b, k is b, and the value of k which is equal to b is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and m) and two binary strings (a and b) of lengths n and m, respectively. It then finds the maximum number of characters in string a that can be matched with characters in string b, in order, without reusing any characters in string b. The function prints this maximum number for each test case.

