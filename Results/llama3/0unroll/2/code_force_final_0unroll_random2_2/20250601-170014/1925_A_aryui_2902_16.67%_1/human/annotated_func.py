#State of the program right berfore the function call: stdin contains one integer t (1 ≤ t ≤ 676) denoting the number of test cases, followed by t lines, each containing two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that is a repetition of the first k characters of the string 'abcdefghijklmnopqrstuvw', repeated n times, where k is an integer between 1 and 26 inclusive, and n is an integer between 1 and 26 inclusive.

#Overall this is what the function does:The function generates a string by repeating the first k characters of the alphabet (from 'a' to 'z') n times, where k and n are integers between 1 and 26 inclusive, and returns this repeated string.

