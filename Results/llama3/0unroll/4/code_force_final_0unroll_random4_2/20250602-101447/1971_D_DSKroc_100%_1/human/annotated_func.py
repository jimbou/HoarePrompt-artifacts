#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings s (1 <= |s| <= 500) consisting of characters 0 and 1.
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        flag = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) != int(s[i + 1]):
                count += 1
            if int(s[i]) < int(s[i + 1]):
                flag = 1
        
        if flag == 0:
            print(count + 1)
        else:
            print(count)
        
    #State: The output state is a series of integers, each representing the number of alternating sequences of 0s and 1s in the corresponding input string. The number of integers in the output state is equal to the value of `t`.

#Overall this is what the function does:This function reads an integer `t` from standard input, followed by `t` strings consisting of characters 0 and 1. It then calculates the number of alternating sequences of 0s and 1s in each string and prints the result for each string. If a string consists of only one type of character (either 0 or 1), it prints the length of the string plus one. Otherwise, it prints the number of alternating sequences. The function outputs a series of integers, each representing the number of alternating sequences in the corresponding input string, with the number of integers equal to the value of `t`.

