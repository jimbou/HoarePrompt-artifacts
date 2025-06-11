#State of the program right berfore the function call: stdin contains one input: an integer
    return int(input())
    #The program returns an integer that was provided as input from stdin

#Overall this is what the function does:The function reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers, where each integer is a result of converting a string from the input to an integer, and the input is a space-separated list of integers from stdin.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts each string to an integer, and returns a map object containing the list of integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were in the input line, separated by spaces.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: a string
    return input()
    #The program returns a string that was provided as input through stdin.

#Overall this is what the function does:The function reads a string from standard input and returns it as is, without any modifications or processing, effectively echoing the input string.

#State of the program right berfore the function call: stdin contains a string of space-separated values of any type and value.
    return input().split()
    #The program returns a list of strings, where each string is a space-separated value from the input string in stdin, and the type and value of each string can be any type and value.

#Overall this is what the function does:Reads a string of space-separated values from standard input and returns a list of strings, where each string is a space-separated value from the input string, without any type or value restrictions.

