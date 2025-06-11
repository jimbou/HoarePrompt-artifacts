#State of the program right berfore the function call: stdin contains one input: a non-empty string consisting only of characters "(" and ")" and representing a balanced parentheses sequence with its length not exceeding 500,000.
    s = input()
    balance = 0
    details = []
    for (i, char) in enumerate(s):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        details.append((balance, -i, char))
        
    #State: Output State: s is a non-empty string consisting only of characters "(" and ")" and representing a balanced parentheses sequence with its length not exceeding 500,000, balance is 0, details is a list of tuples containing the balance, negative index, and character at each position in the string, stdin is empty.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: a string consisting of the characters in s, rearranged based on their balance and negative index

#Overall this is what the function does:The function takes a non-empty string of balanced parentheses from standard input, rearranges the characters based on their balance and negative index, and prints the rearranged string. The function does not return any value, and its purpose is to output a transformed version of the input string.

