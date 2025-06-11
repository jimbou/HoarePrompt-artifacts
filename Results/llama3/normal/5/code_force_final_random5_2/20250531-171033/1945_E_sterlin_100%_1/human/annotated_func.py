#State of the program right berfore the function call: stdin contains one input: an integer
    return int(input())
    #The program returns an integer that was provided as input from stdin.

#Overall this is what the function does:Reads an integer from standard input and returns it as output, effectively passing the input integer through the program without modification.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a list of integers, where each integer is a result of converting a string from the input to an integer, and the input is a space-separated list of integers from stdin.

#Overall this is what the function does:Reads a space-separated list of integers from standard input, converts each string to an integer, and returns a map object containing the list of integers.

#State of the program right berfore the function call: stdin contains a line of space-separated integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were in the input line of space-separated integers.

#Overall this is what the function does:Reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains one input: a string
    return input()
    #The program returns the string that was provided as input from stdin.

#Overall this is what the function does:The function reads a string from standard input and returns it as is, without any modifications or processing, effectively echoing the input string.

#State of the program right berfore the function call: stdin contains a space-separated list of strings
    return input().split()
    #The program returns a list of strings that were space-separated in the input.

#Overall this is what the function does:The function reads a line of input from the standard input, splits it into a list of strings separated by spaces, and returns this list.

