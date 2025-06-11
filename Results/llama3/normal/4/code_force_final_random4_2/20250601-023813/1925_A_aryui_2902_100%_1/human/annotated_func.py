#State of the program right berfore the function call: stdin contains two inputs: two positive integers n and k, where 1 <= n <= 26 and 1 <= k <= 26.
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string that consists of the first k characters of the alphabet string 'abcdefghijklmnopqrstuvwxyz', repeated n times.

#Overall this is what the function does:The function takes two positive integers n and k as input, where 1 <= n <= 26 and 1 <= k <= 26, and returns a string consisting of the first k characters of the alphabet, repeated n times.

