#State of the program right berfore the function call: stdin contains a sequence of lines where the first line contains a single integer t (1 ≤ t ≤ 10^4), and each of the following t lines contains a single integer n (2 ≤ n ≤ 500), followed by a line containing n-1 integers x_2, ..., x_n (1 ≤ x_i ≤ 500).
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: The output state will be a sequence of lines where each line contains a sequence of integers. The number of lines will be equal to the value of t in the initial state. Each line will contain n integers, where n is the value of n in the corresponding iteration of the loop. The integers in each line will be the cumulative sum of the integers in the corresponding line of the initial state, starting from 1000.

#Overall this is what the function does:This function reads a sequence of lines from standard input, where the first line contains an integer t, representing the number of test cases. For each test case, it reads an integer n, followed by n-1 integers. It then calculates the cumulative sum of these integers, starting from 1000, and prints the resulting sequence of integers. The function repeats this process for each test case, producing a sequence of lines as output, where each line contains the cumulative sum of the corresponding input line.

