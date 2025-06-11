#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (2 <= n <= 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases t (1 <= t <= 500) is given in the first line of the input.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: t is an integer between 1 and 500 (inclusive), _ is t, n is an integer between 2 and 10^5 (inclusive), a is a list of n integers between 1 and 10^9 (inclusive), max is the maximum of the minimum of all adjacent pairs of elements in a, i is n - 1, and stdin contains no test cases, and the maximum of the minimum of all adjacent pairs of elements in a which is max is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then finds the maximum of the minimum of all adjacent pairs of elements in the list and prints this value for each test case. The function processes all test cases and does not return any value.

