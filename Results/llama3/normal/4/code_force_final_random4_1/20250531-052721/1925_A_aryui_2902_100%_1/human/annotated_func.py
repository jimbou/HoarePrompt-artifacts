#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 676). Each of the following t lines contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string that consists of the first k characters of the alphabet 'abcdefghijklmnopqrstuvwxyz', repeated n times. The value of k is an integer between 1 and 26, and the value of n is an integer between 1 and 26.

#Overall this is what the function does:This function generates a string consisting of the first k characters of the alphabet, repeated n times, where k and n are integers between 1 and 26, and returns this string.

