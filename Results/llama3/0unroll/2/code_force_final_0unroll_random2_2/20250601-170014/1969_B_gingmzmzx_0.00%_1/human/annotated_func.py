#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t binary strings s (2 <= |s| <= 2 * 10^5).
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
        
    #State: The output state will be the sum of the number of 1's in each binary string s, multiplied by the number of 0's in the same string, plus the number of 0's in each string.

#Overall this is what the function does:The function reads a series of binary strings from standard input, calculates the sum of the products of the number of 1's and 0's in each string, and prints the total sum. It processes multiple strings based on an initial input count, and for each string, it counts the occurrences of 1's and 0's, then calculates the sum of the products of these counts. The final output is the cumulative sum of these products across all input strings.

