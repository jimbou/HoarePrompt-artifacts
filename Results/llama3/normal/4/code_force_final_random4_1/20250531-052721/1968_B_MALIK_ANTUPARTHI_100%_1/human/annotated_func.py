#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 2 * 10^5) followed by two binary strings a and b of lengths n and m, respectively.
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e[k:].index(d[j]) + 1 + k
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: a is an integer between 1 and 10^4, i is a - 1, b is an integer between 1 and 2 * 10^5, c is an integer between 1 and 2 * 10^5, d is a binary string of length between 1 and 2 * 10^5, e is a binary string of length between 1 and 2 * 10^5, j is b, k is b, and the value of k which is equal to b is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and m) and two binary strings (a and b) of lengths n and m, respectively. It then finds the maximum number of characters in string a that can be matched with a substring of string b, and prints this value for each test case.

