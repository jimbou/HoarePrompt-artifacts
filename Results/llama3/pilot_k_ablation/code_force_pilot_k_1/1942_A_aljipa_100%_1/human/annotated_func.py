#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t pairs of integers n and k (1 <= k <= n <= 10^3).
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(1, n + 1) if k == 1 else [-1]
        
        print(*res)
        
    #State: t is an integer between 1 and 10^3, stdin is empty, _ is t, n is an integer between 1 and 10^3, k is an integer between 1 and 10^3, res is a list of integers with a length of n, where all elements are 1 if k is equal to n, all elements are a range from 1 to n if k is 1, and all elements are -1 otherwise, and the elements of the list res are printed for each pair of n and k

#Overall this is what the function does:This function reads a series of input pairs from the standard input, where each pair consists of two integers n and k. It then generates a list of integers based on the values of n and k, and prints this list. The list contains all 1's if k is equal to n, a range of numbers from 1 to n if k is 1, and all -1's otherwise. The function repeats this process for a number of times specified by the first input integer t, and then terminates, leaving the standard input empty.

