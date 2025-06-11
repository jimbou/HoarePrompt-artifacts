#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t strings s consisting of lowercase Latin characters (1 <= |s| <= 10^6).
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
        
    #State: The output state is a list of strings, where each string is either 'YES' or 'NO', indicating whether the corresponding input string can be split into two substrings that are not equal to the first character of the string. If the string can be split, the output also includes the number of splits (1 or 2) and the resulting substrings. The output state has the same length as the input list of strings.

#Overall this is what the function does:This function takes a list of strings as input, where each string consists of lowercase Latin characters. It checks each string to determine if it can be split into two substrings that do not start with the same character as the original string. If such a split is possible, it outputs 'YES', the number of splits (1 or 2), and the resulting substrings. If no such split is possible, it outputs 'NO'. The function processes multiple input strings and returns a list of output strings, each corresponding to the result of the split check for the respective input string.

