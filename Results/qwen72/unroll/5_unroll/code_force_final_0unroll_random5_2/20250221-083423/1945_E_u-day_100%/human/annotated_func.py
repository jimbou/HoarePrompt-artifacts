#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads input from the standard input, which is expected to be a string of space-separated integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains the integers converted from the string of space-separated integers provided by the user.
#Overall this is what the function does:Reads a string of space-separated integers from the standard input and returns a map object containing these integers. The function does not modify any external variables or state.

#State of the program right berfore the function call: No variables are passed to the function func_2, and it depends on the output of func_1 to return a list.
def func_2():
    return list(func_1())
    #The program returns a list that is the output of the function `func_1()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the output of the function `func_1`. After the function concludes, the program state includes a list that was generated by `func_1`.

