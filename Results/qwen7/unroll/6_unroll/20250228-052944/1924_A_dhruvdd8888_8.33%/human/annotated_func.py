#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. Additionally, s is a string of length m comprising only the first k lowercase English alphabets. It is guaranteed that the sum of m and the sum of n over all test cases does not exceed 10^6.
def func_1():
    n, k, m = tuple(map(int, input().split()))
    s = input()
    us = set(chr(i + 97) for i in range(k))
    win = set()
    ans = []
    ps = 0
    for i in s:
        if i in us:
            win.add(i)
            if len(win) == k:
                ans.append(i)
                ps += 1
                win.clear()
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^5, `n` is an integer such that 1 ≤ n ≤ 26, `k` is an integer such that 1 ≤ k ≤ 26, `m` is an integer such that 1 ≤ m ≤ 1000, `s` is a string entered by the user, `us` is a set containing the first `k` lowercase letters starting from 'a', `win` is a set containing up to `k` characters from `s` that are in `us`, `ans` is a list containing the last character added to `win` for each complete set of `k` characters from `s` that are in `us`, `ps` is an integer equal to the number of times `win` was cleared.
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES'
    #State: `t` is an integer such that 1 ≤ t ≤ 10^5, `n` is an integer such that 1 ≤ n ≤ 26, `k` is an integer such that 1 ≤ k ≤ 26, `m` is an integer such that 1 ≤ m ≤ 1000, `s` is a string entered by the user, `us` is a set containing the first `k` lowercase letters starting from 'a', `win` is a set containing up to `k` characters from `s` that are in `us`, `ans` is a list containing the last character added to `win` for each complete set of `k` characters from `s` that are in `us`, `ps` is an integer less than `n` equal to the number of times `win` was cleared
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^5, `n` is an integer such that 1 ≤ n ≤ 26, `k` is an integer such that 1 ≤ k ≤ 26, `m` is an integer such that 1 ≤ m ≤ 1000, `s` is a string entered by the user, `us` is a set containing the first `k` lowercase letters starting from 'a', `win` is a set containing up to `k` characters from `s` that are in `us`, `ans` is a list containing the last character added to `win` for each complete set of `k` characters from `s` that are in `us`, `ps` is an integer less than `n` equal to the number of times `win` was cleared, `i` is the last character printed by the loop.
#Overall this is what the function does:The function processes a string `s` consisting of the first `k` lowercase English alphabets and checks if it contains at least `n` sets of `k` characters. If it finds at least `n` such sets, it prints 'YES'. Otherwise, it prints 'NO' and then constructs and prints a string based on the characters in `us` (the first `k` lowercase letters) that were not part of any complete set of `k` characters found in `s`.

