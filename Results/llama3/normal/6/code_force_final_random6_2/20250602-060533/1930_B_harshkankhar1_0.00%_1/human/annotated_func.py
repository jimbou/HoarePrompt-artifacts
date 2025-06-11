#State of the program right berfore the function call: stdin contains two inputs: first an integer (greater than 0) and then multiple lines, each containing a single integer (greater than or equal to 3 and less than or equal to 10^5).
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a list of integers from 1 to the input integer (greater than 0), with all odd-indexed elements reversed

#Overall this is what the function does:Reverses all odd-indexed elements in a list of integers from 1 to a given input integer (greater than 0) and prints the resulting list.

