#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 1000), and the remaining t inputs are strings of lowercase English letters of length at most 10.
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
        
    #State: The loop has executed for the number of times specified by the integer t in the first input from stdin. For each iteration, if the length of the input string s is 1, 'No' is printed. If the length of s is greater than 1 and all characters in s are the same, 'No' is printed. Otherwise, 'Yes' is printed along with either a shuffled version of s or a rotated version of s where the first character is moved to the end.

#Overall this is what the function does:This function reads a series of strings from standard input, where the first input specifies the number of strings to follow. For each string, it checks if the string has a length of 1 or if all characters are the same. If either condition is true, it prints 'No'. Otherwise, it prints 'Yes' followed by a modified version of the string, which is either a shuffled version of the original string or a rotated version where the first character is moved to the end. The function processes the specified number of strings and prints the corresponding output for each one.

