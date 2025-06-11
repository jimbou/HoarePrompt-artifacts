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
        
    #State: The output will be `t` number of integers, each representing the minimum number of operations required to make the corresponding string `s` non-decreasing. If the string is already non-decreasing, the output will be the length of the string.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings of 0s and 1s. It then calculates and prints the minimum number of operations required to make each string non-decreasing. If a string is already non-decreasing, it prints the length of the string. The function performs this calculation for each of the t input strings, printing the result for each.

