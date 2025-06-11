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
        
    #State: The value of variable k is printed to the console for each test case, representing the maximum number of characters that can be matched between the two binary strings a and b. The value of variable a is decremented by 1 after each iteration, and the loop terminates when a becomes 0. The values of variables b, c, d, and e are updated with new values from the input for each iteration.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two binary strings. It then determines the maximum number of characters that can be matched between the two strings, printing this value for each test case. The function iterates over the test cases until all have been processed, at which point it terminates.

