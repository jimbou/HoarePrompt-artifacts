#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t strings s, each consisting of lowercase Latin characters (1 <= |s| <= 10^6).
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
        
        for j in range((n + 1) // 2):
            if s[j] != s[n - 1 - j]:
                print('YES')
                print(1)
                print(string)
                done = True
                break
            if s[j] != x and count < 1:
                count = j
            if count > 0:
                if s[j] != x:
                    if count2 > 0 and count2 < count:
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
        
    #State: t is 0, i is t, stdin is empty, string is an empty string, s is an empty list, x is undefined, n is undefined, j is undefined, count is undefined, count2 is undefined, done is False.

#Overall this is what the function does:This function reads a series of strings from standard input, where each string consists of lowercase Latin characters. It checks each string to determine if it can be split into two non-empty substrings such that the resulting substrings do not contain a specific character (the first character of the original string) or contain it only once. If such a split is possible, it prints 'YES', the number of splits (1 or 2), and the resulting substrings. If no such split is possible, it prints 'NO'. The function processes multiple strings as specified by the initial integer input, which represents the number of strings to follow.

