#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 ≤ t ≤ 676). Each of the following t lines contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that consists of the first k characters of the alphabet 'abcdefghijklmnopqrstuvw', repeated n times, where k and n are integers between 1 and 26 (inclusive), and the total number of repetitions is determined by the value of n, which is between 1 and 676 (inclusive).

#Overall this is what the function does:This function generates a string consisting of the first k characters of the alphabet 'abcdefghijklmnopqrstuvw', repeated n times, where k and n are integers between 1 and 26 (inclusive), and returns the resulting string.

