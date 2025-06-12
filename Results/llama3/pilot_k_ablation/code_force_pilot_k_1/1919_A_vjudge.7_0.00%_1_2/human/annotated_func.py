#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 ≤ t ≤ 1000). Each of the following t lines contains two space-separated integers a and b (1 ≤ a, b ≤ 10^9).
    t = int(input())
    for _rep in range(t):
        n, k = list(map(int, input().split()))
        
        if n > k:
            print('Bob')
        elif n < k:
            print('Alice')
        else:
            print('Bob')
        
    #State: `t` is an integer between 0 and 1000 (inclusive), `_rep` is `t`, `n` and `k` are integers. If `n` is greater than `k`, 'Bob' is printed. If `n` is less than `k`, 'Alice' is printed. If `n` is equal to `k`, 'Bob' is printed. stdin is empty.

#Overall this is what the function does:This function reads input from stdin, expecting a specific format: an integer t followed by t lines, each containing two space-separated integers a and b. It then compares each pair of integers and prints 'Alice' if a is less than b, 'Bob' if a is greater than or equal to b. The function processes all input lines and empties stdin.

