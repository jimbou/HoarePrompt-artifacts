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
        
    #State: The value of variable 'a' is reduced by the number of test cases in stdin, stdin contains no test cases, and the values of variables 'b', 'c', 'd', 'e', 'k' are reset to their initial values (0, 0, empty string, empty string, 0, respectively) after each iteration of the loop.

#Overall this is what the function does:Reads a specified number of test cases from standard input, where each test case consists of two integers and two binary strings, and for each test case, it finds the maximum number of characters in the first binary string that can be matched with a substring of the second binary string, printing this value for each test case.

