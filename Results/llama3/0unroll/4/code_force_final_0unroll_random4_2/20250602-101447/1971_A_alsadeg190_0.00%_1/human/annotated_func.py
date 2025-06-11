#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 100) and then t lines each containing two space-separated integers (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The output will contain x lines, each containing two space-separated integers. The integers on each line will be in non-decreasing order, i.e., the first integer will be less than or equal to the second integer.

#Overall this is what the function does:The function takes an integer t (1 <= t <= 100) as input, followed by t lines of two space-separated integers (0 <= x, y <= 9). It then outputs t lines, each containing the two input integers in non-decreasing order, i.e., the first integer is less than or equal to the second integer.

