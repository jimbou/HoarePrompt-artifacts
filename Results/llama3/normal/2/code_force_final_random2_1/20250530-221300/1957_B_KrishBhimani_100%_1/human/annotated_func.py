#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two integers n and k (1 <= n <= 2 * 10^5, 1 <= k <= 10^9).
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
        
    #State: stdin is empty, t is an integer, for every n and k, if n is 1, the value of k is printed, otherwise, this is printed: (1 << i) - 1, k - ((1 << i) - 1), and n-2 zeros, where i is the number of times temp can be doubled before it is greater than or equal to k.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t representing the number of test cases. For each test case, it reads two integers n and k, and then prints a sequence of numbers based on the values of n and k. If n is 1, it simply prints the value of k. Otherwise, it calculates the largest power of 2 less than or equal to k, subtracts this value from k, and prints the result along with n-2 zeros. The function continues this process until all test cases have been processed, at which point stdin is empty.

