#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 ≤ t ≤ 1000) and then t lines each containing a single integer (2 ≤ X ≤ 10^18).
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = ''
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans = f'{max}' + ' ' + ans
                max -= 1
                x = x // 2
            else:
                ans = f'{min}' + ' ' + ans
                min += 1
                x -= 1
            t += 1
        
        print(t)
        
        print(*ans)
        
    #State: The output state will be the same as the initial state, with the addition of t number of lines, each containing a single integer, and t number of lines, each containing a sequence of integers. The value of t is the input integer provided in the first line of the input. The sequence of integers in each line is the result of the loop's execution, where each integer is either max or min, depending on whether the input integer x is even or odd, respectively. The value of max and min is updated in each iteration of the loop, with max decreasing by 1 and min increasing by 1. The loop continues until x becomes 1.

#Overall this is what the function does:This function reads a series of integers from standard input, applies a transformation to each integer based on whether it is even or odd, and prints the result. For each integer, it generates a sequence of integers by iteratively applying the transformation until the integer becomes 1. The transformation involves decrementing a maximum value (initially 100,000,000) for even integers and incrementing a minimum value (initially -100,000,000) for odd integers. The function then prints the number of iterations performed for each integer, followed by the generated sequence of integers. The function processes multiple integers, with the number of integers specified by the first input integer.

