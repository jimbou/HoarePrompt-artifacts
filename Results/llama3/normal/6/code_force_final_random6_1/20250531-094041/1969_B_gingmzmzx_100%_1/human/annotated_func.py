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
        
    #State: n is an integer equal to 0, _ is equal to n, s is an empty list, c is the last integer in the original list, zeroes is an integer equal to the number of 0s in the original list, cnt is a list of two integers where cnt[0] is equal to the number of 0s in the original list and cnt[1] is equal to the number of 1s in the original list, ans is equal to the total number of 1s in the original list that are not immediately preceded by a 0, stdin contains 0 binary strings, and the total number of 1s in the original list that are not immediately preceded by a 0 which is equal to ans is being printed.

#Overall this is what the function does:This function reads a series of binary strings from standard input, where the first line contains the number of strings to follow, and each subsequent line contains a binary string. It then calculates and prints the total number of 1s in each string that are not immediately preceded by a 0. The function processes all input strings and prints the calculated values for each string.

