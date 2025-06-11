#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000), then t pairs of integers n and k (2 <= n <= 10^6, 1 <= k <= n).
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: The output state will contain `t` number of lines, each containing a sequence of integers. Each sequence will have a length of 21 and will contain the numbers from 1 to 20, with the number at index `i` being replaced by three numbers: `k - (1 << i)`, `k + 1`, and `k + 1 + (1 << i)`. The value of `i` is determined by the largest power of 2 that is less than or equal to `k`. The remaining numbers in the sequence will be powers of 2 from 1 to 20, excluding the number at index `i`.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts two inputs: an integer t and t pairs of integers n and k. For each pair of n and k, it generates a sequence of 21 integers, replacing the number at a specific index with three numbers derived from k, and prints the length and the sequence. The function performs this operation t times, producing t sequences of integers as output.

