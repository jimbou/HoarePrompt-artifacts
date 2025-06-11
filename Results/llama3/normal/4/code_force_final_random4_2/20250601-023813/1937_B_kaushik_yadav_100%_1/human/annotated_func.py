#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two binary strings of the same length as the integer.
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
        
    #State: `t` is undefined, `n` is an integer, `a` is a non-empty string, `b` is a string, `ans` is a string containing the characters of `a` and `b` in an alternating pattern, `i` is equal to the last index of `a`, `work` is False, `j` is equal to the last index of `a` minus 1, `counter` is either 1, 2, or 3, `stdin` is empty, and the string `ans` containing the characters of `a` and `b` in an alternating pattern is being printed, and the value of `counter` which is either 1, 2, or 3 depending on the values of `a[j + 1]` and `b[j]` is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and two binary strings of the same length. It then generates a new string by alternating characters from the two input strings, starting with the first string, and prints this new string. Additionally, it counts the number of consecutive occurrences of a specific pattern in the input strings and prints this count. The function repeats this process for all test cases, consuming all input from standard input.

