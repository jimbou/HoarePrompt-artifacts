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
        
    #State: The loop will execute n times, and in each iteration, it will read a binary string s from the standard input, calculate the number of zeroes in the string, and then iterate over the string to calculate the answer. The answer is calculated by adding 1 to the answer if the current character is 0 and the count of 1's is greater than 0, or by adding the difference between the total number of zeroes and the count of zeroes to the answer if the current character is 1. The answer is then printed to the standard output. After all iterations, the loop will finish, and the program will terminate. The state of the variables outside the loop will remain unchanged.

#Overall this is what the function does:This function reads a series of binary strings from standard input, calculates a specific value for each string based on the occurrences of 0s and 1s, and prints these values to standard output. The function iterates over a specified number of input strings, processing each one independently, and does not modify any external state or variables outside of its own scope.

