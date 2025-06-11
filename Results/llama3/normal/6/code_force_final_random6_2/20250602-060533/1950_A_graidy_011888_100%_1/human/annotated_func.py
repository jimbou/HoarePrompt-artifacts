#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 1000) and then t lines, each containing three digits (0 <= a, b, c <= 9).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `n` is greater than or equal to 0, `i` is `n`, `a`, `b`, `c` are integers assigned from the input, stdin contains no input. If `a` is less than `b` and `b` is less than `c`, then 'STAIR' is printed. If `a` is less than `b` but `b` is greater than `c`, then 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of triple-digit numbers from standard input and classifies each as either 'STAIR', 'PEAK', or 'NONE' based on the relative values of the digits. It prints the classification for each triple-digit number. The function accepts no parameters and returns no value, instead printing the classifications directly to the console.

