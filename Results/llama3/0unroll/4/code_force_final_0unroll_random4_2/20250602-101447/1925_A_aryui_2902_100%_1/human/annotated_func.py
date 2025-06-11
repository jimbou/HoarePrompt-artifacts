#State of the program right berfore the function call: stdin contains two inputs: two positive integers n and k (1 <= n <= 26 and 1 <= k <= 26).
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string that consists of the first k characters of the alphabet 'abcdefghijklmnopqrstuvwxyz', repeated n times.

#Overall this is what the function does:The function generates a string consisting of the first k characters of the alphabet, repeated n times, based on user input of two positive integers n and k, and returns this string.

