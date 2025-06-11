#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer n (2 <= n <= 2 * 10^5), then two binary strings a_11 a_12 ... a_1n and a_21 a_22 ... a_2n (a_1i and a_2i are either 0 or 1). The number of test cases t is between 1 and 10^4.
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        ans = ''
        
        i = 0
        
        work = True
        
        while i < len(a):
            if work:
                ans += a[i]
                if i + 1 < len(a) and b[i] < a[i + 1]:
                    work = False
                elif i + 1 == len(a):
                    ans += b[i]
                    break
                else:
                    i += 1
            else:
                ans += b[i]
                i += 1
        
        print(ans)
        
        counter = 1
        
        for j in range(len(a) - 1):
            if a[j + 1] == b[j]:
                counter += 1
            elif a[j + 1] == '0' and b[j] == '1':
                counter = 1
            else:
                break
        
        print(counter)
        
    #State: `t` is an integer between 1 and 10^4, `_` is `t`, `n` is an integer between 2 and 2 * 10^5, `a` is a binary string of length `n`, `b` is a binary string of length `n`, `ans` is a string that starts with the first character of `a` and ends with the character at index `n-1` of `a` or `b`, `i` is `n`, `work` is True or False, `j` is `n-1`, `counter` is either `n` or `n-1` depending on the values of `a[j + 1]` and `b[j]`, and the value of `ans` and the value of `counter` are being printed, and the stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and two binary strings a and b of length n. It then constructs a new string ans by starting with the first character of a and appending characters from a and b based on certain conditions. The function prints the constructed string ans and a counter value, which is either n or n-1 depending on the values of a and b. The function processes all test cases and prints the results for each case.

