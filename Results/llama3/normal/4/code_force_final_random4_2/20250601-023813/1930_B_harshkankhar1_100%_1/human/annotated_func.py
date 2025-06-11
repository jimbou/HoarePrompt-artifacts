#State of the program right berfore the function call: stdin contains two inputs: first an integer (greater than 0) and then multiple lines each containing a single integer (greater than or equal to 3 and less than or equal to 10^5).
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: the elements of the list a (where the elements are integers from 1 to the input integer in reverse order for even indices and in ascending order for odd indices)

#Overall this is what the function does:Reverses elements at even indices in a list of integers from 1 to a user-specified number (greater than 0) and prints the modified list, where elements at even indices are in reverse order and elements at odd indices are in ascending order.

