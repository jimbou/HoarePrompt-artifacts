#State of the program right berfore the function call: n is an integer such that 2 <= n <= 500, c and d are integers such that 1 <= c, d <= 10^6, and l is a list of n^2 integers where each integer b_i satisfies 1 <= b_i <= 10^9. The sum of n^2 over all test cases does not exceed 25 * 10^4.
def func_1(n, c, d, l):
    a = min(l)
    li = []
    for k in range(0, n):
        for h in range(0, n):
            li.append(a + k * c + d * h)
        
    #State: `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, and `l` is a list of n^2 integers where each integer b_i satisfies 1 <= b_i <= 10^9; `a` is the minimum value in the list `l`; `li` is a list of n^2 integers where each integer is calculated as a + k * c + d * h for k, h in the range from 0 to n-1.
    li.sort()
    l.sort()
    if (l == li) :
        return 'yes'
        #The program returns 'yes'
    #State: `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, `l` is a sorted list of n^2 integers where each integer b_i satisfies 1 <= b_i <= 10^9; `a` is the minimum value in the list `l`; `li` is a sorted list of n^2 integers where each integer is calculated as a + k * c + d * h for k, h in the range from 0 to n-1`. The list `l` is not equal to the list `li`.
    return 'no'
    #The program returns 'no'
#Overall this is what the function does:The function `func_1` checks if a given list `l` of `n^2` integers can be rearranged to match a specific sequence generated by starting from the minimum value in `l` and incrementing by `c` and `d` in a grid-like fashion. It returns 'yes' if the list can be rearranged to match this sequence, otherwise it returns 'no'.

