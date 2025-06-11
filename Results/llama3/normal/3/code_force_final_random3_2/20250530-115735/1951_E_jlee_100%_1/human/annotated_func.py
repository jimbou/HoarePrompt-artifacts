#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases. Each test case contains a string s consisting of lowercase Latin characters (1 ≤ |s| ≤ 10^6). The sum of |s| over all test cases does not exceed 10^6.
    t = int(input())
    for i in range(t):
        string = input()
        
        s = list(string)
        
        n = len(s)
        
        done = False
        
        if n == 1:
            print('NO')
            continue
        
        x = s[0]
        
        if x != s[-1]:
            print('YES')
            print(1)
            print(string)
            continue
        
        if s.count(x) == n:
            print('NO')
            continue
        elif s.count(x) == n - 1:
            if n % 2 == 1 and s[(n - 1) // 2] != x:
                print('NO')
            else:
                print('YES')
                print(1)
                print(string)
            continue
        
        count = 0
        
        count2 = 0
        
        for j in range(n):
            if s[j] != s[n - 1 - j]:
                print('YES')
                print(1)
                print(string)
                done = True
                break
            if s[j] != x and count < 1:
                count = j
                continue
            if count > 0:
                if s[j] != x:
                    if count2 < count:
                        print('YES')
                        print(2)
                        print(string[:j], string[j:])
                        done = True
                        break
                    elif count2 == count:
                        if count > 1:
                            print('YES')
                            print(2)
                            print(string[:j - 1], string[j - 1:])
                            done = True
                            break
                        else:
                            count2 = 0
                            continue
                    elif count2 > count:
                        print('YES')
                        print(2)
                        print(string[:j], string[j:])
                        done = True
                        break
                else:
                    count2 += 1
        
        if not done:
            print('NO')
        
    #State: t is an integer between 0 and 10^4 (exclusive), i is t, s is a list of characters from the input string, n is the length of s, x is the first character of s, string is the input string, j is n, done is True.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case is a string of lowercase Latin characters. It then checks if the string can be split into two substrings by removing at most one character, such that the resulting substrings are equal. If possible, it prints 'YES' and the number of characters to remove, followed by the modified string. If not possible, it prints 'NO'. The function processes all test cases and prints the results accordingly.

