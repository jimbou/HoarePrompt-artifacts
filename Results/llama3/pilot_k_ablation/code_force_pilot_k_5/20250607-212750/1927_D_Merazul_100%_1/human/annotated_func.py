#State of the program right berfore the function call: stdin contains a sequence of lines. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains an integer n (2 <= n <= 2 * 10^5), then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6), then an integer q (1 <= q <= 2 * 10^5), and finally q pairs of integers l and r (1 <= l < r <= n).
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        R()
        
        a = [0]
        
        p = i = j = 0
        
        for x in R():
            j = (j, i)[x != p]
            a += j,
            p = x
            i += 1
        
        q, = R()
        
        while q:
            q -= 1
            l, r = R()
            print(*((a[r], r), [-1] * 2)[a[r] < l])
        
    #State: t is 0, a is a list containing n+1 elements: 0 and n copies of j, p is the last element in R(), i is n, j is either 0 or n-1 depending on whether the last element in R() is equal to the second last element in R(), l and r are the first and second elements in R() respectively, q is 0, x is the last element in R(), and either (a[r], r) or [-1, -1] is printed depending on whether a[r] is less than l.

#Overall this is what the function does:This function reads a sequence of lines from standard input, where the first line contains an integer t, and each of the following t lines contains an integer n, followed by n integers, an integer q, and q pairs of integers. It then processes each line, creating a list a of length n+1, where a[i] is the index of the last occurrence of the i-th integer in the input sequence. For each pair of integers l and r, it prints either the value of a[r] and r, or [-1, -1] if a[r] is less than l. The function repeats this process t times, and finally, it prints the results for all pairs of integers.

