#State of the program right berfore the function call: stdin contains one input: a non-negative integer.
    return int(input())
    #The program returns a non-negative integer that was provided as input.

#Overall this is what the function does:The function reads a non-negative integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a value from the space-separated list of integers provided in the standard input (stdin).

#Overall this is what the function does:The function reads a space-separated list of integers from the standard input (stdin), converts each integer to an integer type, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains a list of space-separated integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were space-separated in the input.

#Overall this is what the function does:The function reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return sorted(list(map(int, input().split())))
    #The program returns a list of integers sorted in ascending order, where the integers are obtained from the space-separated list of integers in stdin.

#Overall this is what the function does:Reads a space-separated list of integers from standard input, converts them to integers, sorts them in ascending order, and returns the sorted list.

#State of the program right berfore the function call: stdin contains a space-separated list of strings
    return map(str, input().split())
    #The program returns a map object containing a list of strings, where each string is a word from the space-separated list of strings in stdin.

#Overall this is what the function does:The function reads a space-separated list of strings from standard input, splits it into individual words, and returns a map object containing these words as strings.

#State of the program right berfore the function call: stdin contains a string
    return list(input())
    #The program returns a list of characters from the string in stdin.

#Overall this is what the function does:The function reads a string from standard input and returns it as a list of characters.

#State of the program right berfore the function call: stdin contains a space-separated list of strings.
    return sorted(list(map(str, input().split())))
    #The program returns a list of strings from the input, sorted in ascending order. The list contains all the strings that were in the input, each string is a separate element in the list, and the strings are arranged in alphabetical order.

#Overall this is what the function does:This function reads a space-separated list of strings from standard input, splits it into individual strings, sorts them in alphabetical order, and returns the sorted list of strings.

#State of the program right berfore the function call: arr is a list of non-zero positive integers.
    ans = []
    tem = 1
    for i in range(len(arr)):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: Output State: arr is a list of non-zero positive integers, ans is a list of cumulative products of elements in arr, tem is the product of all elements in arr.
    return ans
    #The program returns a list of cumulative products of elements in a list of non-zero positive integers.

#Overall this is what the function does:This function calculates and returns a list of cumulative products of elements in a given list of non-zero positive integers. The input list remains unchanged. The function produces a new list where each element at index i is the product of all elements in the input list up to index i.

#State of the program right berfore the function call: arr is a list of non-zero integers.
    ans = []
    tem = 1
    for i in range(len(arr) - 1, -1, -1):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: ans is a list of the cumulative product of the elements of arr in reverse order, tem is the product of all elements in arr, arr remains unchanged.
    return ans
    #The program returns a list of the cumulative product of the elements of arr in reverse order.

#Overall this is what the function does:The function accepts a list of non-zero integers as input and returns a new list containing the cumulative product of the input list's elements in reverse order, without modifying the original input list.

