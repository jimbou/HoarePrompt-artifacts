#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the length of the permutations). Each integer in the list is greater than or equal to 3 and less than or equal to 10^5. The sum of these integers does not exceed 10^5.
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: a list of integers from 1 to the input number, with every other element reversed

#Overall this is what the function does:The function generates a list of integers from 1 to a user-specified number, reverses every other element in the list, and prints the modified list. The input number is expected to be a positive integer, and the function does not validate or handle invalid inputs. The function does not return any value; it only prints the result to the console.

