#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t binary strings s (2 <= |s| <= 2 * 10^5; s_i in {0, 1}).
    n = int(input())
    for _ in range(n):
        s = list(map(int, input().strip()))
        
        zeroes = s.count(0)
        
        cnt = [0, 0]
        
        ans = 0
        
        for c in s:
            cnt[c] += 1
            if c == 0:
                ans += 1 if cnt[1] > 0 else 0
            else:
                ans += zeroes - cnt[0]
        
        print(ans)
        
    #State: The loop will execute n times, and in each iteration, it will read a binary string s from the standard input, calculate the number of zeroes in the string, and then iterate over the string to calculate the number of pairs of adjacent 0s and 1s. The result will be printed to the standard output. After all iterations, the loop will finish, and the program will terminate. The value of n will be unchanged, and the standard input will be empty.

#Overall this is what the function does:This function reads a series of binary strings from standard input, calculates the number of pairs of adjacent 0s and 1s in each string, and prints the result to standard output. It repeats this process for a specified number of iterations, then terminates.

