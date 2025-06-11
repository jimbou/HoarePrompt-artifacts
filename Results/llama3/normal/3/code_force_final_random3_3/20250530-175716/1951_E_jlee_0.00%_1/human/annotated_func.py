#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains a string s consisting of lowercase Latin characters (1 <= |s| <= 10^6).
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
        
    #State: t is an integer between 0 and 10^4 (inclusive), i is t, stdin contains 0 lines of input, string is a string consisting of lowercase Latin characters (1 <= |string| <= 10^6), s is a list of characters, x is the first character of s, count is either 0 or greater than 0, count2 is either 0 or greater than 0, done is True, n is the length of the string s and must be greater than 0, j is (n+1)//2.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t (1 <= t <= 10^4) and each of the following t lines contains a string s consisting of lowercase Latin characters (1 <= |s| <= 10^6). It then checks each string to determine if it can be split into two substrings that are the same when reversed. If such a split is possible, it prints 'YES', the number of splits required (1 or 2), and the resulting substrings. If no such split is possible, it prints 'NO'. The function processes all input strings and prints the results for each one.

