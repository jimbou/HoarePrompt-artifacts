#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples, each containing an integer n (1 ≤ n ≤ 10) and a string s of length n, where s consists of characters 'W' or 'B', and at least one cell is black.
def func_1():
    ma = mi = 0
    m = int(input())
    s = input()
    c = d = 0
    l = []
    for j in s:
        c += 1
        
        if j == 'B':
            mi = c
            break
        
    #State: `c` is the position of the first 'B' in `s` (or the length of `s` if 'B' is not found), `d` is 0, `ma` is 0, `mi` is the position of the first 'B' in `s` (or 0 if 'B' is not found), `m` is the input integer, `s` is the input string, `l` is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `c` is the position of the first 'B' in `s` (or the length of `s` if 'B' is not found), `d` is the position of the last 'B' in `s` (or the length of `s` if 'B' is not found) + 1, `ma` is the position of the last 'B' in `s` (or 0 if 'B' is not found), `mi` is the position of the first 'B' in `s` (or 0 if 'B' is not found), `m` is the input integer, `s` is the input string, `l` is an empty list.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' and the position of the first 'B' in the string `s`, plus 2. If 'B' is not found in `s`, the program returns 2.
#Overall this is what the function does:The function `func_1` takes no parameters and reads an integer `m` and a string `s` from the user. It returns the difference between the position of the last 'B' and the position of the first 'B' in the string `s`, plus 2. If 'B' is not found in `s`, the function returns 2.

