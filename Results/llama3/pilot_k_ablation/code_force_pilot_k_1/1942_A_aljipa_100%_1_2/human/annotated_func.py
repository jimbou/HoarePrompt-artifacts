#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t pairs of integers n and k (1 <= k <= n <= 10^3).
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(1, n + 1) if k == 1 else [-1]
        
        print(*res)
        
    #State: `t` is 0, `_` is `t`, `n` and `k` are the last pair of integers read from stdin, `res` is a list of integers that is either all 1s, a range from 1 to `n`, or all -1s, depending on the last pair of integers read from stdin.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where each pair consists of a number n and a number k. For each pair, it generates a list of integers based on the values of n and k. If k is equal to n, the list contains all 1s. If k is 1, the list contains a range of numbers from 1 to n. For any other values of k, the list contains all -1s. The function then prints each generated list.

