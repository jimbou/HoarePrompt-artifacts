#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains an integer t (1 <= t <= 10^4) — the number of test cases. Each test case contains a string s consisting of lowercase Latin characters (1 <= |s| <= 10^6). The sum of |s| over all test cases does not exceed 10^6.
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
        
    #State: The output state after the loop executes all the iterations is that the input string `s` has been processed and the result of whether it can be split into two substrings with different characters at the same position has been printed. The value of `t` remains unchanged, and the input string `s` has been modified to contain the result of the processing. The output state is a series of 'YES' or 'NO' indicating whether the string can be split, followed by the split position and the resulting substrings if 'YES', or just 'NO' if the string cannot be split.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case is a string of lowercase Latin characters. It checks if the string can be split into two substrings with different characters at the same position. If possible, it prints 'YES', the split position, and the resulting substrings; otherwise, it prints 'NO'. The function handles various cases, including strings with only one character, strings with all characters the same, and strings with an odd or even length. It iterates through the string to find the split position, if any, and prints the result accordingly.

