#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B'.
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
        
    #State: Output State: `ma` is 0, `mi` is 0, `c` is the length of `s`, `d` is 0, `m` is an input integer, `s` is an input string, `l` is an empty list.
    #
    #Explanation: The loop increments `c` for each character in the string `s`. If the character 'B' is encountered, `mi` is set to the current value of `c` and the loop breaks. Since no specific values for `s` are given, `c` will be the length of `s` after the loop completes, assuming 'B' was not found or the loop did not break. The variables `ma`, `d`, `m`, and `l` remain unchanged as they are not affected by the loop.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: Output State: `ma` is the distance from the end of the string `s` where the character 'B' is found, `mi` is 0, `c` is the length of `s`, `d` is the number of characters processed before finding 'B', `m` is an input integer, `s` is an input string, `l` is an empty list.
    return ma - mi + 2
    #The program returns the distance from the end of the string `s` where the character 'B' is found, which is `ma`, minus 0 (the value of `mi`), plus 2.
#Overall this is what the function does:The function processes a string `s` consisting of characters 'W' and 'B', where at least one character is 'B'. It calculates the distance from the end of the string to the last occurrence of 'B' and returns this distance plus 2. The function does not accept any parameters and reads `m` and `s` from input.

