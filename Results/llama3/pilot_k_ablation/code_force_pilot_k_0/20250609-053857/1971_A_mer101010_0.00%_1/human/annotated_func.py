#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    n = int(input())
    t = 0
    for i in range(n):
        a, b = map(int, input().split())
        
        if a > b:
            print(a, ' ', b)
        elif a == b:
            print(a, ' ', b)
        else:
            print(b, ' ', a)
        
    #State: Output State: The output state is a series of n lines, each containing two space-separated integers. For each line, the first integer is the maximum of the two input integers x and y, and the second integer is the minimum of the two input integers x and y. The value of n remains unchanged, and t remains 0.

#Overall this is what the function does:The function reads an integer n from standard input, followed by n lines of input, each containing two space-separated integers. It then prints n lines of output, where each line contains the maximum and minimum of the two input integers, in that order. The function does not modify the value of n or any other external state.

