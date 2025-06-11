#State of the program right berfore the function call: stdin contains two inputs: first an integer (greater than 0) and then multiple integers (each greater than or equal to 3).
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: a sequence of numbers from 1 to the input integer, with every other number reversed, separated by spaces

#Overall this is what the function does:The function reads an integer from standard input, generates a sequence of numbers from 1 to the input integer, reverses every other number in the sequence, and prints the modified sequence separated by spaces.

