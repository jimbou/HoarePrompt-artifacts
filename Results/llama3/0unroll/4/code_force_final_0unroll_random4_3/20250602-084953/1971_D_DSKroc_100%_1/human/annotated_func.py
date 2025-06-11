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
        
    #State: The output state will contain t integers, each representing the minimum number of operations required to make the corresponding input string s a string of alternating 0s and 1s. The operations allowed are flipping a single character (i.e., changing 0 to 1 or 1 to 0). The output integers will be printed on separate lines.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases, followed by t strings of 0s and 1s. For each string, it calculates the minimum number of operations (flipping a single character) required to make the string alternate between 0s and 1s. The function then prints the result for each string on a separate line, with the output being the minimum number of operations needed to achieve the alternating pattern.

