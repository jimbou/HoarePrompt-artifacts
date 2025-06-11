#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 50000), then t pairs of integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * k - 1))
                break
            tot += a
            k -= tot
            pow *= 2
        
    #State: t is 0, stdin contains 0 pairs of integers n and k (1 <= k <= 10^9), n is 0, k is an integer, L is an empty list, m is 0, tot is 0, pow is 1.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where each pair represents a number n and a position k. For each pair, it calculates and prints the kth number in a sequence derived from n, using a binary representation. The function processes all input pairs and does not return any value, only producing output for each pair.

