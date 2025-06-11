#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 5 * 10^4) and then t pairs of integers n and k (1 <= k <= n <= 10^9).
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
        
    #State: t is an integer equal to 0, n is an integer equal to 0, k is an integer equal to 0, L is an empty list, a is the last element of L, m is an integer equal to 0, tot is an integer equal to the sum of all elements in L, pow is an integer equal to 2 to the power of the number of elements in L, stdin contains 0 pairs of integers.

#Overall this is what the function does:This function reads input from stdin, processes t pairs of integers (n, k), and prints the result of a calculation involving these pairs. It appears to perform some sort of binary search or bit manipulation, as it uses powers of 2 and bit shifting operations. The function does not return any value, but instead prints the results directly to the console. The input variables (t, n, k) are consumed and left in a state of 0, indicating that they are no longer needed after the function concludes.

