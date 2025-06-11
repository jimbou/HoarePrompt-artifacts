#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (2 <= n <= 10^6, 1 <= k <= n).
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: t is an integer greater than or equal to 0 and less than or equal to 1000, tc is equal to t, n is an integer between 2 and 10^6 inclusive, k is an integer between 1 and n inclusive, i is the greatest integer less than or equal to log2(k), ans is a list containing twenty-one integers: k - (1 << i), k + 1, k + 1 + (1 << i), and 1 << j for all j in range(20) where j is not equal to i, stdin contains at least t lines, each containing two integers, and the length of the list ans which is 21 is being printed, and the elements of the list ans which are k - (1 << i), k + 1, k + 1 + (1 << i), and 1 << j for all j in range(20) where j is not equal to i are being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it generates a list of 21 integers based on the values of n and k, and then prints the length of the list followed by the list elements. The list contains the numbers k - (1 << i), k + 1, k + 1 + (1 << i), and 1 << j for all j in range(20) where j is not equal to i, where i is the greatest integer less than or equal to log2(k). The function repeats this process for the specified number of test cases.

