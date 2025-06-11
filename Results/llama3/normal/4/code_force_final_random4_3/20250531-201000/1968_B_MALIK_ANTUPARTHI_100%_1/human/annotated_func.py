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
        
    #State: `a` is an integer between 1 and 10^4, `i` is equal to `a`, `b` is an integer, `c` is an integer, `d` is a string, `e` is a string, `j` is equal to `b`, and `k` is equal to `b`, and the value of `k` which is equal to `b` is being printed, stdin contains 0 test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers and two binary strings. It then iterates through the first binary string, checking for the presence of each character in the second binary string. If a character is found, it updates a counter to the index of the found character in the second string plus one. If a character is not found or the end of the first string is reached, it prints the current counter value and moves on to the next test case. After processing all test cases, the function terminates, leaving the input stream empty.

