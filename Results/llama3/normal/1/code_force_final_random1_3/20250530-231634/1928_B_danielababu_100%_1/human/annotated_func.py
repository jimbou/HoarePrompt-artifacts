#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    return int(input())
    #The program returns an integer greater than 0 that was provided as input.

#Overall this is what the function does:The function reads an integer from standard input and returns it. The returned integer is guaranteed to be greater than 0.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return map(int, input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a value from the space-separated list of integers provided in the standard input (stdin).

#Overall this is what the function does:The function reads a space-separated list of integers from the standard input, converts each integer to an integer type, and returns a map object containing the sequence of integers.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as input in the stdin, separated by spaces.

#Overall this is what the function does:Reads a list of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: stdin contains a space-separated list of integers.
    return sorted(list(map(int, input().split())))
    #The program returns a sorted list of integers that were provided as input in the stdin, in ascending order.

#Overall this is what the function does:The function reads a space-separated list of integers from standard input, sorts them in ascending order, and returns the sorted list.

#State of the program right berfore the function call: stdin contains a space-separated list of strings.
    return map(str, input().split())
    #The program returns a map object that contains a space-separated list of strings from the standard input, where each string is converted to a string type.

#Overall this is what the function does:The function reads a space-separated list of strings from the standard input, converts each string to a string type, and returns a map object containing the converted strings.

#State of the program right berfore the function call: stdin contains a string
    return list(input())
    #The program returns a list of characters from the string in stdin

#Overall this is what the function does:Reads a string from standard input and returns it as a list of characters.

#State of the program right berfore the function call: stdin contains a list of strings separated by spaces.
    return sorted(list(map(str, input().split())))
    #The program returns a list of strings that were in the stdin, sorted in ascending order, where each string is separated by a space.

#Overall this is what the function does:This function reads a list of strings from standard input, sorts them in ascending order, and returns the sorted list.

#State of the program right berfore the function call: arr is a list of positive integers.
    ans = []
    tem = 1
    for i in range(len(arr)):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: arr is a list of positive integers, ans is a list containing the product of all elements of arr up to each index, tem is the product of all elements of arr, i is len(arr) - 1
    return ans
    #The program returns a list 'ans' containing the product of all elements of list 'arr' up to each index.

#Overall this is what the function does:This function takes a list of positive integers as input and returns a new list where each element at index i is the product of all elements in the input list up to index i. The input list remains unchanged.

#State of the program right berfore the function call: arr is a list of non-negative integers.
    ans = []
    tem = 1
    for i in range(len(arr) - 1, -1, -1):
        tem *= arr[i]
        
        ans.append(tem)
        
    #State: arr is a list of non-negative integers, ans is a list containing the product of all elements of arr, tem is the product of all elements of arr, i is -1
    return ans
    #The program returns a list containing the product of all non-negative integers in the list 'arr'.

#Overall this is what the function does:The function takes a list of non-negative integers as input and returns a new list containing the cumulative product of all elements in the input list, in reverse order. The input list remains unchanged.

