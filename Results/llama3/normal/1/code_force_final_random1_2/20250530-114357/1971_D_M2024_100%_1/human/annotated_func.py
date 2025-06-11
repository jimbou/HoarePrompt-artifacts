#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500 (inclusive).
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
        
    #State: t is an integer equal to 0, stdin contains 0 strings, _ is t, a is a string consisting of characters '0' and '1' with length between 1 and 500 (inclusive), i is -1, cut0 is the number of times '0' is followed by '1' in a, cut1 is the number of times '1' is followed by '0' in a. If cut0 is 0, the value of cut1 + 1 is printed. Otherwise, the sum of cut0 and cut1 (the total number of cuts in string a) is printed.

#Overall this is what the function does:This function reads a series of binary strings from standard input, counts the number of transitions between '0' and '1' in each string, and prints the total number of transitions plus one if the string starts with '0', or just the total number of transitions if the string starts with '1'.

