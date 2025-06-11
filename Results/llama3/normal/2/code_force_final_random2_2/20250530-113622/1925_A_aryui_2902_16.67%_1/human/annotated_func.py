#State of the program right berfore the function call: stdin contains two inputs: two positive integers n and k (1 ≤ n ≤ 26 and 1 ≤ k ≤ 26).
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that is a repetition of the first k characters of the alphabet, repeated n times.

#Overall this is what the function does:This function takes two positive integers n and k as input from the user, where 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and returns a string that is a repetition of the first k characters of the alphabet, repeated n times.

