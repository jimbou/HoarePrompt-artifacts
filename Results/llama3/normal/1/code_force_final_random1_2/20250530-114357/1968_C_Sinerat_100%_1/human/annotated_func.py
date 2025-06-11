#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains a single integer n (2 ≤ n ≤ 500). Each of the following t lines contains n-1 integers x_2, …, x_n (1 ≤ x_i ≤ 500).
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: n is an integer, x is a list of integers, a is a list of n integers where the first element is 1000 and the remaining elements are the cumulative sum of x, i is n-1, _ is t-1, stdin contains no lines of input, and the list a is being printed, where a contains 1000 and the cumulative sum of the list x.

#Overall this is what the function does:The function reads multiple lines of input from stdin, where the first line contains an integer t, and each of the following t lines contains an integer n and n-1 integers. It then calculates the cumulative sum of the integers for each set of n-1 integers, prepending 1000 to each set, and prints the resulting lists. The function repeats this process t times, consuming all input from stdin.

