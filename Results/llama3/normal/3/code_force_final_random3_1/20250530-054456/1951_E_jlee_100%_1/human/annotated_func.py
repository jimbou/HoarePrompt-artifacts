#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t strings, each consisting of lowercase Latin characters (1 <= |s| <= 10^6). The sum of |s| over all test cases does not exceed 10^6.
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
        
    #State: t is an integer between 1 and 10^4, i is t-1, stdin contains 0 strings, each consisting of lowercase Latin characters (1 <= |s| <= 10^6), string is a string consisting of lowercase Latin characters (1 <= |s| <= 10^6), s is a list of characters in the string, j is n, n is greater than or equal to 0, count is n, count2 is n, and if the current value of done is False, 'NO' is printed.

#Overall this is what the function does:This function reads a series of strings from standard input, where the first line contains the number of strings (t) and each subsequent line contains a string consisting of lowercase Latin characters. For each string, it checks if the string can be split into two non-empty substrings such that the first substring is a palindrome and the second substring is not equal to the first character of the original string. If such a split is possible, it prints 'YES', the number of splits (1 or 2), and the resulting substrings. If no such split is possible, it prints 'NO'. The function processes all input strings and prints the results for each string.

