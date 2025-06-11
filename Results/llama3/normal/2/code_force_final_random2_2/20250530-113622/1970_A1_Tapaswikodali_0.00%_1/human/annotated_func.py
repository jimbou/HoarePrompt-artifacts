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
        
    #State: `s` is a non-empty string consisting only of characters "(" and ")" that is a balanced parentheses sequence with its length not exceeding 500,000, `char` is the last character in the string, `i` is the length of the string minus 1, `balance` is 0, and `details` is a list containing tuples with the balance, the negative of the index, and the character at each index.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: the original string s

#Overall this is what the function does:The function reads a non-empty string of balanced parentheses from standard input, sorts the string based on the balance of parentheses at each position, and prints the sorted string. The function does not modify the input string or its balance, but rather rearranges the characters to maintain the original balance while sorting. The output is the original string, which is a balanced parentheses sequence with its length not exceeding 500,000.

