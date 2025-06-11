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
        
    #State: Output State: The loop has executed q times, and for each iteration, it has printed one of the strings 'STAIR', 'PEAK', or 'NONE' to the console based on the values of a, b, and c. The values of q and mn remain unchanged.

#Overall this is what the function does:The function reads an integer q from standard input, followed by q lines of input, each containing three digits a, b, and c. It then prints one of the strings 'STAIR', 'PEAK', or 'NONE' to the console for each line of input, based on the values of a, b, and c. The function does not return any value or modify any external state, only producing output to the console.

