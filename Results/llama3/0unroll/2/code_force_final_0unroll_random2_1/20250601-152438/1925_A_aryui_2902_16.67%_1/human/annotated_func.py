#State of the program right berfore the function call: stdin contains one integer t (1 ≤ t ≤ 676) denoting the number of test cases. For each test case, stdin contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that consists of the first k characters of the alphabet, repeated n times. The value of k is between 1 and 26 inclusive, and the value of n is between 1 and 26 inclusive.

#Overall this is what the function does:The function generates a string consisting of the first k characters of the alphabet, repeated n times, where k and n are integers between 1 and 26 inclusive, and returns this string.

