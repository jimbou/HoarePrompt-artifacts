#State of the program right berfore the function call: num is a list of integers where 1 <= len(num) <= 2 * 10^5, and each integer in num is within the range 1 <= a_i <= 10^9.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `counter` is the number of trailing zeros in the list `num`.
    return counter
    #The program returns the number of trailing zeros in the list `num`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `num` and returns the number of trailing zeros in the list. The list `num` remains unchanged after the function call.

