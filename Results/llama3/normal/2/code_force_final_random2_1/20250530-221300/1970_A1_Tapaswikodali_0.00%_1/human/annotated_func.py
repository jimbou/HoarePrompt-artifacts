#State of the program right berfore the function call: stdin contains one input: a non-empty string consisting only of characters "(" and ")" and is a balanced parentheses sequence with its length not exceeding 500,000.
    s = input()
    balance = 0
    details = []
    for (i, char) in enumerate(s):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        details.append((balance, -i, char))
        
    #State: `s` is an empty string, `details` is a list containing tuples of three elements: the balance (0), the negative index of each character in the original string, and each character in the original string, `stdin` is empty, `i` is the length of the original string minus 1, and `balance` is 0.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: the string containing the characters of the original string in the sorted order based on their negative indices

#Overall this is what the function does:This function reads a balanced parentheses sequence from standard input, sorts the characters based on their original order (from last to first), and prints the sorted string. The function does not return any value, but instead, prints the result directly. The input string is assumed to be non-empty and consists only of "(" and ")" characters, with a length not exceeding 500,000.

