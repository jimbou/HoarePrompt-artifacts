#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing three digits a, b, c (0 <= a, b, c <= 9).
    q = int(input())
    mn = 100
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        
        if a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: q is 0, mn is 100, i is q, a, b, c are integers between 0 and 9, stdin is empty. If the current values of a, b, and c are such that a is less than b and b is less than c, then 'STAIR' is printed. If a is less than b and b is greater than c, then 'PEAK' is printed. In all other cases, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of three-digit numbers from standard input, classifies each number as either 'STAIR', 'PEAK', or 'NONE' based on the relative values of its digits, and prints the classification for each number. It does not return any value or modify any external state, and its only effect is the output printed to the console.

