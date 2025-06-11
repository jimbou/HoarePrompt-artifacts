#State of the program right berfore the function call: stdin contains one input: two positive integers n and k, separated by a space.
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that consists of the first k characters of the string 'abcdefghijklmnopqrstuvw', repeated n times.

#Overall this is what the function does:The function accepts two positive integers, n and k, as input and returns a string consisting of the first k characters of the alphabet, repeated n times.

