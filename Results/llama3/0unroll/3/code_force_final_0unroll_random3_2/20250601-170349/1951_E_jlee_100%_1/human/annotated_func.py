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
        
    #State: The output state will be a series of 'YES' or 'NO' strings, each followed by either a single string (if 'YES' and the string can be split into two parts at the first character) or two strings (if 'YES' and the string can be split into two parts at a position other than the first character), or no additional strings (if 'NO'). The number of 'YES' or 'NO' strings will be equal to the initial value of `t`.

#Overall this is what the function does:This function reads a series of strings from standard input, determines whether each string can be split into two parts that are identical when reversed, and prints the result. If a string can be split, it prints 'YES', the number of parts, and the parts themselves; otherwise, it prints 'NO'. The function processes multiple strings, with the number of strings specified by the first input value.

