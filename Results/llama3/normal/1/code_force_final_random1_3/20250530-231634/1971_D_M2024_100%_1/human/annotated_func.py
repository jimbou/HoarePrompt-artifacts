#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings s (1 <= |s| <= 500) consisting of characters 0 and 1.
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut0 = 0
        
        cut1 = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut1 += 1
            if a[i] == '0' and a[i + 1] == '1':
                cut0 += 1
        
        if cut0 == 0:
            print(cut1 + 1)
        else:
            print(cut0 + cut1)
        
    #State: t is an integer between 0 and 500 (inclusive), a is a string consisting of characters 0 and 1 that must have at least len(a) characters, cut0 is the total number of times '0' is followed by '1' in a, cut1 is the total number of times '1' is followed by '0' in a, _ is t, i is len(a) - 1, stdin contains 0 strings. If cut0 is 0, the value of cut1 + 1 is printed. Otherwise, the sum of cut0 and cut1 is printed.

#Overall this is what the function does:The function reads a series of strings from standard input, each consisting of characters '0' and '1', and for each string, it counts the number of times '0' is followed by '1' and '1' is followed by '0'. If a string contains no instances of '0' followed by '1', it prints the number of times '1' is followed by '0' plus one. Otherwise, it prints the total number of both instances. The function processes multiple strings as specified by an initial integer input.

