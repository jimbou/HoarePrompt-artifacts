#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two binary strings of the same length. The length of the strings is equal to the integer. The integer is greater than or equal to 2 and less than or equal to 2 * 10^5. The sum of the lengths of the strings over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer greater than or equal to 0, `n` is an integer between 2 and 2 * 10^5 inclusive, `a` is a binary string of length `n`, `b` is a binary string of length `n`, `ans` is a string of length `n` that is being printed, `i` is equal to `n`, `j` is equal to `n - 1`, and `counter` is an integer greater than or equal to 1, and the value of counter which is greater than or equal to 1 is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and two binary strings of the same length. It then generates a new string by combining the two input strings in a specific way, based on the values of the characters in the strings, and prints this new string. Additionally, it counts the number of consecutive positions where the second string has a '1' and the first string has a '0', and prints this count. The function processes all test cases and prints the results for each case.

