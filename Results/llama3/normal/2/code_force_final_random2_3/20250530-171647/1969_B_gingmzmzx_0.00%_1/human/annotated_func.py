#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a binary string (a string consisting of only 0-s and/or 1-s) for each test case. The length of the binary string is between 2 and 2 * 10^5 (inclusive). The sum of lengths of strings over all test cases doesn't exceed 2 * 10^5.
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
        
    #State: `n` is 0, `s` is an empty list of integers representing the binary string, `zeroes` is the total number of zeroes in the binary string, `cnt` is a list containing the total count of zeroes and ones in the binary string, `ans` is the total number of times a 1 is followed by a 0 in the binary string, and `c` is the last element in the list `s` which is now counted `n` times in `cnt[c]`.

#Overall this is what the function does:This function reads a series of binary strings from standard input, where each string is preceded by the number of test cases. For each binary string, it counts the total number of times a 1 is followed by a 0 and prints this count. The function processes all test cases and does not return any value, only producing output through print statements.

