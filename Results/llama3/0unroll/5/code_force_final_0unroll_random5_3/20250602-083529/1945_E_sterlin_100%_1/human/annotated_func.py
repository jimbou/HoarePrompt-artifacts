#State of the program right berfore the function call: stdin contains one input: an integer
    return int(input())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it as output.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, which are the result of converting each space-separated integer from the input into an integer.

#Overall this is what the function does:Reads a space-separated list of integers from standard input and returns a map object containing the converted integers.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as a space-separated list in the standard input.

#Overall this is what the function does:Reads a space-separated list of integers from the standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: a string
    return input()
    #The program returns a string that was provided as input from stdin.

#Overall this is what the function does:The function reads a string from standard input and returns it as is, without any modifications or processing, effectively echoing the input string.

#State of the program right berfore the function call: stdin contains a string of space-separated values of any type and value.
    return input().split()
    #The program returns a list of strings, where each string is a space-separated value from the input string in stdin.

#Overall this is what the function does:The function reads a string of space-separated values from standard input, splits it into individual values, and returns them as a list of strings.

