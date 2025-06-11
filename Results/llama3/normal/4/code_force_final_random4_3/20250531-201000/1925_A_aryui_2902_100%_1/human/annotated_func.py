#State of the program right berfore the function call: stdin contains one input: two positive integers n and k separated by a space, where 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string that consists of the first k characters of the alphabet 'abcdefghijklmnopqrstuvwxyz' repeated n times.

#Overall this is what the function does:The function accepts two positive integers n and k as input from the user, where 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and returns a string consisting of the first k characters of the alphabet 'abcdefghijklmnopqrstuvwxyz' repeated n times.

