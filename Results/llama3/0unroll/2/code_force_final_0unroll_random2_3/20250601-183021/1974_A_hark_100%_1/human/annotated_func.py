#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4), then t lines each containing two space-separated integers x and y (0 <= x, y <= 99).
    ap = int(input())
    for k in range(ap):
        x, y = map(int, input().split())
        
        if x > 0 and y > 0:
            bxsfory = math.ceil(y / 2)
            x = x - bxsfory * 15 + y * 4
            bxsfory1 = 0 if x <= 0 else math.ceil(x / 15)
            print(bxsfory1 + bxsfory)
        elif x == 0 and y > 0:
            print(math.ceil(y / 2))
        elif x > 0 and y == 0:
            print(math.ceil(x / 15))
        else:
            print(0)
        
    #State: Output State: The output state after the loop executes all the iterations will be a series of printed values, each representing the total number of boxes needed for a given pair of x and y values. The exact values will depend on the input provided in the stdin.

#Overall this is what the function does:Calculates and prints the total number of boxes needed for each pair of input values x and y, based on specific rules, and outputs the results for all input pairs.

