#State of the program right berfore the function call: stdin contains one input: an integer (greater than 1).
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: The loop will output the maximum number of pairs of numbers that can be formed from the input numbers, where the first number in each pair is less than the second number. The output will be in the format "k best", where k is the first number in the pair and best is the second number in the pair. The output will be repeated for each iteration of the outer loop.

#Overall this is what the function does:The function reads an integer from standard input, representing the number of test cases. For each test case, it reads another integer n, and then performs a series of comparisons and outputs to find and print the maximum number of pairs of numbers that can be formed from the input numbers, where the first number in each pair is less than the second number. The output is in the format "k best", where k is the first number in the pair and best is the second number in the pair. This process is repeated for each iteration of the outer loop.

