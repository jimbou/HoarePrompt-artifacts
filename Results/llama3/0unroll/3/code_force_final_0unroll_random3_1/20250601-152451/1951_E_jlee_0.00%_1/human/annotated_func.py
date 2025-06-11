#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t strings, each consisting of lowercase Latin characters (1 <= |s| <= 10^6).
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
        
    #State: The output state will be a series of 'YES' or 'NO' strings, each followed by either a single string (if 'YES' and the string can be split into two substrings with the same characters) or two strings (if 'YES' and the string can be split into two substrings with different characters), or no additional strings (if 'NO'). The number of 'YES' or 'NO' strings will be equal to the initial value of t. The strings will be the result of checking each input string for the conditions specified in the loop.

#Overall this is what the function does:This function reads a series of strings from standard input, checks each string for specific conditions, and outputs whether the string can be split into two substrings with the same or different characters. If the string can be split, it outputs the split substrings; otherwise, it outputs 'NO'. The function processes multiple strings based on the initial input value 't', which specifies the number of strings to process.

