#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 10^3) and then t lines each containing an integer (3 <= n <= 10^5).
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a list of integers from 1 to t where elements at even indices are in reverse order

#Overall this is what the function does:Reverses elements at even indices in a list of integers from 1 to t, where t is a user-provided integer between 1 and 10^3, and prints the modified list.

