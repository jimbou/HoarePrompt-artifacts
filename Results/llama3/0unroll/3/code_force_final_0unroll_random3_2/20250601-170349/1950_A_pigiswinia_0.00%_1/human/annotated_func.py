#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= integer <= 1000) and then  integer triplets (0 <= integers <= 9) equal to the first integer.
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The loop will print out either 'STAIRS', 'PEAK', or 'NONE' for each of the t integer triplets in the stdin, depending on the values of a, b, and c in each triplet. The value of t remains unchanged.

#Overall this is what the function does:This function reads a series of integer triplets from standard input, determines the relationship between the three integers in each triplet, and prints out a corresponding classification ('STAIRS', 'PEAK', or 'NONE') for each triplet. The function does not modify the input values or return any values, but instead provides a printed output for each triplet based on its characteristics.

