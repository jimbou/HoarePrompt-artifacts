#State of the program right berfore the function call: stdin contains one input: a non-empty string consisting only of characters "(" and ")" that is a balanced parentheses sequence with its length not exceeding 500,000.
    s = input()
    balance = 0
    details = []
    for (i, char) in enumerate(s):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        details.append((balance, -i, char))
        
    #State: Output State: The string s remains unchanged, the balance is 0, the details list contains tuples of the balance, negative index, and character at each position in the string s, and the stdin remains empty.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s (the original string s, unchanged)

#Overall this is what the function does:This function reads a balanced parentheses sequence from standard input, processes it, and prints the original sequence back to the console. The function does not modify the input string and does not have any side effects on the input variables. The function's purpose is to read, process, and echo back the input string, leaving the input variables unchanged.

