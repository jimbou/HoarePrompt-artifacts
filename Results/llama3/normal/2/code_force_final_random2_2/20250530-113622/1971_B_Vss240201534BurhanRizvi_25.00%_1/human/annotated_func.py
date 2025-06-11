#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= integer <= 1000) and then a string of lowercase English letters of length at most 10.
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: _ is the integer input from stdin, stdin is empty, s is a string of lowercase English letters of length at most 10, s2 is a string of the same letters as s but in a random order. If s is not equal to s2, 'Yes' is printed and s2 is printed. If s is equal to s2, 'No' is printed.

#Overall this is what the function does:The function reads an integer and a string from standard input, generates a random permutation of the string, and prints 'Yes' followed by the permutation if it is different from the original string, or 'No' if it is the same. The function repeats this process for the number of times specified by the input integer.

