#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing a binary string s (2 <= |s| <= 2 * 10^5).
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
        
    #State: n is an integer between 0 and 10^4 (inclusive), stdin is empty, _ is n, s is an empty list, c is the last integer in the list s, zeroes is the count of zeroes in the list s, cnt is a list of two integers where cnt[0] is the count of zeroes in the list s and cnt[1] is the count of ones in the list s, ans is the sum of the counts of ones in the list s and the count of zeroes in the list s minus the count of zeroes in the list s, and ans is printed which is equal to the sum of the counts of ones in the list s and the count of zeroes in the list s minus the count of zeroes in the list s.

#Overall this is what the function does:This function reads a series of binary strings from standard input, calculates the sum of the counts of ones and the count of zeroes minus the count of zeroes for each string, and prints the result for each string. The function accepts no parameters and returns no value, instead printing the calculated sums to standard output.

