#State of the program right berfore the function call: stdin contains one input: a non-empty string consisting only of characters "(" and ")" and its length does not exceed 500,000. The string is a balanced parentheses sequence.
    s = input()
    balance = 0
    details = []
    for (i, char) in enumerate(s):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        details.append((balance, -i, char))
        
    #State: stdin is empty, s is a non-empty string consisting only of characters "(" and ")" and its length does not exceed 500,000, balance is 0, details is a list of tuples containing the balance, negative index, and character at each position in the string s.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: a string containing the characters from s in the order specified by the sorted details list

#Overall this is what the function does:The function reads a balanced parentheses sequence from standard input, sorts the characters based on their balance and position in the string, and prints the sorted characters in a single string. The input string is consumed from standard input, and the output string is printed to the console. The function does not return any value.

