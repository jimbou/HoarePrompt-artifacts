#State of the program right berfore the function call: t is an integer such that 1 <= t <= 676, and for each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns the first `k` characters of the string `'abcdefghijklmnopqrstuvwxyz'` repeated `n` times.
#Overall this is what the function does:The function reads two integers `n` and `k` from the input, and returns a string consisting of the first `k` characters of the alphabet repeated `n` times.

