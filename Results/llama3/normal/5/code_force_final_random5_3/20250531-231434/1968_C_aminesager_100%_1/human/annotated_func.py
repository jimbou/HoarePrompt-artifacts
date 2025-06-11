#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (2 <= n <= 500), then n-1 integers x_2,...,x_n (1 <= x_i <= 500).
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] + T[i - 1])
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: t is 0, n is an integer between 2 and 500 (inclusive), T is a list of n-1 integers between 1 and 500 (inclusive), a is a list containing n integers: 1000, 1000 + T[0], 1000 + T[0] + T[1], ..., 1000 + sum(T), i is n-1, result is a string containing the elements of a separated by spaces, and the string result containing the elements of a separated by spaces is printed, stdin contains no input.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and n-1 integers x_2 to x_n. It then calculates a list of n integers, where the first element is 1000 and each subsequent element is the sum of the previous element and the corresponding x_i. Finally, it prints the calculated list as a string of space-separated integers. The function repeats this process until all test cases have been read from standard input.

