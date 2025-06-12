#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9).
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b and b % 2 != 0 or b / 2 == a and a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    #State: `n` is an integer between 1 and 10^4 (inclusive), `i` is `n`, `a` and `b` are integers between 1 and 10^9 (inclusive), stdin is empty. The loop has printed 'YES' or 'NO' for each pair of integers in the input, based on the conditions specified in the loop.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where the first line specifies the number of pairs, and then for each pair, it checks if the numbers meet certain conditions and prints 'YES' if they do and 'NO' if they don't. The conditions for printing 'YES' are that either both numbers are even or one is twice the other and the other is odd. After processing all pairs, the function leaves the standard input empty.

