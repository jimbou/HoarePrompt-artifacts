#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two binary strings of the same length equal to the integer.
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
            if a[j + 1] == '0' and b[j] == '1':
                counter = 1
        
        print(counter)
        
    #State: `t` is 0, `_` is `t`, `n` is an integer, `a` is a non-empty string, `b` is a string, `ans` is either a combination of `a` and the last character of `b` if `work` is True and the length of `a` is equal to the length of `b`, or just `b` if `work` is False, `i` is equal to the length of `a`, `work` is either True or False, `counter` is 1 plus the number of times `a[j + 1]` is equal to `b[j]` minus the number of times `a[j + 1]` is '0' and `b[j]` is '1', stdin is empty, and `j` is equal to the length of `a` minus 1.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and two binary strings of the same length. It then processes each test case by combining the two binary strings into a single string, `ans`, based on certain conditions. The function prints the combined string `ans` and a counter value, which is calculated by comparing the characters of the two input strings. The function repeats this process for all test cases until standard input is empty.

