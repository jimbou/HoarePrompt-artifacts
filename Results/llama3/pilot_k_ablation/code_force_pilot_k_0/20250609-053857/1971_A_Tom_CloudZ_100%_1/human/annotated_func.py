#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(min(a, b), max(a, b))
        
    #State: The loop will print t lines, each containing two space-separated integers. The first integer in each line will be the smaller of the two input integers x and y, and the second integer will be the larger of the two input integers x and y. The value of t remains unchanged.

#Overall this is what the function does:The function reads an integer t from standard input, followed by t lines of input, each containing two space-separated integers x and y. It then prints t lines, each containing the smaller and larger of the two input integers x and y, in that order, without modifying the value of t.

