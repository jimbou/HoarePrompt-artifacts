#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^4. s is a string of length n consisting of the characters 'L' and 'R'. The sum of all n across all test cases does not exceed 2·10^5.
def func_1(n, m, a, s):
    b = []
    l = 0
    r = n - 1
    for i in range(n):
        if s[i] == 'L':
            b.append(a[l])
            l += 1
        else:
            b.append(a[r])
            r -= 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 1 ≤ n ≤ 2·10^5; `m` is an integer such that 1 ≤ m ≤ 10^4; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ a_i ≤ 10^4; `s` is a string of length `n` consisting of the characters 'L' and 'R'; `b` is a list containing all elements of `a` in the order specified by `s`; `l` is `n`; `r` is `-1`.
    ans = []
    p = 1
    for v in reversed(b):
        p = p * v % m
        
        ans.append(p)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 1 ≤ n ≤ 2·10^5; `m` is an integer such that 1 ≤ m ≤ 10^4; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ a_i ≤ 10^4; `s` is a string of length `n` consisting of the characters 'L' and 'R'; `b` is a list containing all elements of `a` in the order specified by `s`; `l` is `n`; `r` is `-1`; `ans` is a list of length `n` where each element is the cumulative product of elements in `b` in reverse order, modulo `m`; `p` is the product of all elements in `b` in reverse order, modulo `m`.
    return reversed(ans)
    #The program returns the list `ans` in reverse order, where each element of `ans` is the cumulative product of elements in `b` in reverse order, modulo `m`.
#Overall this is what the function does:The function `func_1` takes four parameters: `n` (the length of list `a` and string `s`), `m` (a modulus), `a` (a list of `n` integers), and `s` (a string of length `n` consisting of 'L' and 'R'). It constructs a new list `b` by selecting elements from `a` based on the direction specified in `s`, then computes a list `ans` where each element is the cumulative product of elements in `b` in reverse order, modulo `m`. Finally, it returns the list `ans` in reverse order.

