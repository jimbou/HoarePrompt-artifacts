#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer n (2 <= n <= 2 * 10^5), then two binary strings of length n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is 0, `_` is `t`, `n` is undefined, `a` is undefined, `b` is undefined, `ans` is undefined, `i` is undefined, `work` is undefined, `stdin` is empty, `j` is undefined, `counter` is undefined.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n and two binary strings of length n. It then constructs a new string by concatenating characters from the two input strings based on certain conditions, and prints this new string. Additionally, it counts the number of consecutive positions where the two input strings have the same character, and prints this count. The function processes all test cases and leaves the standard input empty after execution.

