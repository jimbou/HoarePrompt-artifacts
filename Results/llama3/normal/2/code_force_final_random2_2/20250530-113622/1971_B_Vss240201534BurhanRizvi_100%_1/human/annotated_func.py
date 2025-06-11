#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters and having a length of at most 10.
    for _ in range(int(input())):
        s = input()
        
        if len(s) == 1:
            print('No')
        elif len(set(s)) == 1 and len(s) > 1:
            print('No')
        else:
            s2 = ''.join(random.sample(s, len(s)))
            if s == s2:
                s2 = s[1:] + s[0]
            print('Yes')
            print(s2)
        
    #State: Output State: `_` is equal to the initial value of `t`, stdin is empty.
    #
    #The loop will execute for the number of times specified by the initial value of `t`. After each iteration, the loop will consume one string from the input and print either 'No' or 'Yes' followed by a modified string. Once all strings have been consumed, the loop will terminate, leaving stdin empty. The value of `_` will be equal to the initial value of `t`, indicating the number of iterations that have taken place.

#Overall this is what the function does:This function reads a specified number of strings from standard input, checks each string for uniqueness of characters, and prints either 'No' if the string has only one unique character or all characters are the same, or 'Yes' followed by a modified version of the string where the first character is moved to the end if the shuffled string is identical to the original. After processing all input strings, the function leaves the standard input empty.

