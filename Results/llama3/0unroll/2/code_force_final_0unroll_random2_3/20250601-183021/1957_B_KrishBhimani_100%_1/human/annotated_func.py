#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers n and k (1 <= n <= 2 * 10^5, 1 <= k <= 10^9).
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        if n == 1:
            print(k)
        else:
            arr = []
            k0 = k
            i = 0
            ans = []
            temp = 1
            while True:
                if temp * 2 < k:
                    temp *= 2
                    i += 1
                else:
                    break
            ans.append((1 << i) - 1)
            ans.append(k - sum(ans))
            ans += [0] * (n - len(ans))
            print(*ans)
        
    #State: The output state will be a list of integers, where each integer represents the result of the calculation for each test case. The list will have a length of t, where t is the number of test cases. Each integer in the list will be the result of the calculation (1 << i) - 1 + k - sum(ans), where i is the number of times the while loop iterates, k is the input value, and ans is the list of values calculated in the while loop. The list will be in the format [result1, result2, ..., resultt], where result1, result2, ..., resultt are the results of the calculation for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and k. For each test case, it calculates a list of integers based on the values of n and k. If n is 1, the function simply prints the value of k. Otherwise, it calculates a list of integers by finding the largest power of 2 less than k, subtracting the sum of the calculated list from k, and appending zeros to the list until its length is equal to n. The function then prints the calculated list for each test case.

