#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains a single integer n (2 <= n <= 2 * 10^5). The second and third lines contain a binary string a_{11} a_{12} ... a_{1n} and a_{21} a_{22} ... a_{2n} respectively (a_{1i} and a_{2i} are either 0 or 1). The number of test cases is between 1 and 10^4.
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
        
    #State: t is 0, _ is t, n is an integer, a is a non-empty string, b is a string, ans is a string containing either the first character of a or the first character of b followed by the character at index i of a or b and possibly the character at index i of a or b and the character at index i of a or b, i is equal to the length of a, work is False, the string ans is being printed, j is equal to the length of a minus 1, and counter is equal to the number of times a[j + 1] is equal to b[j] plus 1, or 1 if a[j + 1] is '0' and b[j] is '1', and counter is printed, counter (where counter is the number of times a[j + 1] is equal to b[j] plus 1, or 1 if a[j + 1] is '0' and b[j] is '1').

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: an integer n, and two binary strings a and b of length n. It then constructs a new string ans by concatenating characters from a and b based on certain conditions. The function prints the constructed string ans and a counter value, which represents the number of times a specific condition is met in the strings a and b. The function repeats this process for each test case.

