#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers x and y (0 <= x, y <= 99).
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: The loop will execute 'a' times, each time reading two integers from stdin, performing some calculations, and printing the result. The value of 'a' will be unchanged, and stdin will be empty after the loop finishes. The output will be 'a' lines, each containing an integer.

#Overall this is what the function does:This function reads an integer 't' from standard input, followed by 't' lines each containing two integers 'x' and 'y'. It then performs calculations using these integers and prints the result for each pair. The function does not return any value, but instead, outputs 't' lines to the standard output, each containing a calculated integer. The input values 'x' and 'y' are not modified, and the input stream is consumed until it is empty.

